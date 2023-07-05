import time

from threading import Thread
from multiprocessing import Process, Queue


# 간단한 MultiThreading 구조 설계
# 1. 동시에 한개의 변수에 1을 더해주는 두개의 흐름을 만듦
GLOBAL_VAR_1 = 0


# Thread로 작동할 함수부
def add_one():
    # Thread가 접근할 변수를 전역화
    global GLOBAL_VAR_1
    for i in range(1000):
        GLOBAL_VAR_1 += 1


if __name__ == "__main__":
    th_1 = Thread(target=add_one)   # 각 Thread가 실행할 함수의 주소를 지정(호출 X)
    th_2 = Thread(target=add_one)
    th_1.start()    # 각 Thread의 시작시점을 지정
    th_2.start()
    th_1.join()     # 각 Thread의 종료를 기다림.
    th_2.join()
    # print(GLOBAL_VAR_1)  # 종료 후 변수의 값 확인


# 한 변수에 영향을 주었는데 정상적으로 작동했다? 이게 어떻게 된 것일까?
# 이를 이해하기 위해선 start()를 처리하는 동안 이전 Thread는 아직 돌고 있다는 것을 명심해야한다.
# 이를 보기 위해서 다음과 같이 횟수를 늘려보겠다.
GLOBAL_VAR_2 = 0


# Thread로 작동할 함수부
def add_one_():
    # Thread가 접근할 변수를 전역화
    global GLOBAL_VAR_2
    for i in range(1000000):
        GLOBAL_VAR_2 += 1


if __name__ == "__main__":
    th_1 = Thread(target=add_one_)   # 각 Thread가 실행할 함수의 주소를 지정(호출 X)
    th_2 = Thread(target=add_one_)
    th_1.start()    # 각 Thread의 시작시점을 지정
    th_2.start()
    th_1.join()     # 각 Thread의 종료를 기다림.
    th_2.join()
    # print(GLOBAL_VAR_2)  # 종료 후 변수의 값 확인
"""
위 코드는 이상합니다. 우선 3.10버전 이전까지만해도 위 식에서 발생하는 문제는 명확했습니다. 바로, 
공유자원으로 인한 부정확한 MultiThread작동이라는 문제가 있었습니다. 예제코드야 카페에 있습니다.
그런데 갑자기 잘 작동합니다. 이 문제는 본래 뮤텍스가 되지 않아 문제가 발생해야합니다. 간단히 말해서
병렬성이라는 것은 어떤 것을 정의하는지부터 이해해야합니다.
우리는 코드 a += 1을 해결하기 위해서는 우선 현재 메모리에 있는 a값을 가져와야합니다. 그래야 그 값에서
1을 더한 값을 줄 수 있으니까요. 그런데 thread는 사이좋게 작동하는 것이 아닙니다. 저마다 자기가 하고 싶은
데로 작동합니다. 첫 thread가 위 연산을 하고 있는 중에 다음 thread가 이 자원을 가지고 오면 아직 연산되지
않은 상태가 넘어옵니다. 그런데 가져간 후에 첫 thread가 계산이 끝나고 값을 다시 메모리에 할당합니다.
a의 값이 정해졌고 다시 그 a값을 가져와 계산을 할 것입니다. 그 사이에 두번째 thread의 계산이 끝나 돌아왔을
때, 이 때의 값은 이전 a의 값에서 1을 더한, 즉 이미 메모리에 할당된 수와 같은 상태입니다.
이런 공유자원에 Lock이 걸려있지 않아 생기는 문제가 있는 문제였습니다. 그런데 웬일인지, 마치 Lock을 걸지도
않았는데 Lock이 걸린것처럼 작동합니다. 이건 문제가 있습니다.
"""

"""
이 문제에 대하여 'thread-safe'하냐는 질문을 하게 됩니다. thread-safe란 것은 thread가 데이터에 동시에
접근하면서 생기는 문제가 없을 때를 지칭하는 말입니다. 그리고 이 뜻대로면 위 식은 thread-safe합니다.
그런데 그래선 안되는 문제가 있습니다. python 3.10버전 이전에는 lock이 없다면 당연한 문제였습니다.
그런데 이젠 아니군요. 이건 python에서 일부 연산에 대해서 lock을 자연스럽게 연결해주기 때문입니다.
자 그럼 이걸 어떻게 증명할 수 있을까요? 연산식을 우선 바꿔보겠습니다.
"""
GLOBAL_VAR_3 = 0


# Thread로 작동할 함수부
def add_one_2():
    # Thread가 접근할 변수를 전역화
    global GLOBAL_VAR_3
    for i in range(1000000):
        GLOBAL_VAR_3 += int(True)


if __name__ == "__main__":
    start = time.time()
    th_1 = Thread(target=add_one_2)   # 각 Thread가 실행할 함수의 주소를 지정(호출 X)
    th_2 = Thread(target=add_one_2)
    th_1.start()    # 각 Thread의 시작시점을 지정
    th_2.start()
    th_1.join()     # 각 Thread의 종료를 기다림.
    th_2.join()
    # print(GLOBAL_VAR_3)  # 종료 후 변수의 값 확인
    # print(time.time() - start)
"""
다행이도 이렇게 작동하게 되면 thread-safe하지 않은 결과가 정상적으로 발생했습니다. 문제가 발생한 것이
정상이라는 것이 이해되지 않을테지만 이게 컴퓨터 구조상 맞는 thread 결과일 것입니다.
아래식을 통해 시간과 값으로 비교하면 이해하기 편할 것입니다.
"""
if __name__ == "__main__":
    GLOBAL_VAR_3 = 0
    start = time.time()
    add_one_2()
    add_one_2()
    # print(GLOBAL_VAR_3)  # 종료 후 변수의 값 확인
    # print(time.time() - start)
"""
우선 위를 이해하기 위해서 GIL을 기억해야합니다. python은 thread로 이상적인 병렬처리가 되지 않습니다.
자 그럼 보면 알겠지만 값은 다르지만 서로 시간은 같습니다.
이런 상태에서 보면 공유자원에 대한 문제는 발생했고 발생했건 안했건 둘간의 속도 차이가 얼마 나지 않은
것을 알 수 있습니다. 덕분에 우리는 python이 병렬처리는 안되지만 thread가 겪는 문제는 겪는, 즉 thread가
존재는 한다는 것을 알 수 있게 되었습니다.
다만, 일부의 경우에서만 thread-safe하게 작동해서 정상적으로 느낄 뿐이죠.
"""

"""
그럼 병렬성을 완벽하게 보장하기 위해서 Process를 쓴다는데 어떻게 쓸까요?
사용 방법은 별반 차이는 없습니다. 다만, 이제 공유자원을 쓰기가 어려워진다는 단점이 발생합니다.
말했지만 둘은 별개의 프로세스입니다. 이 말인 즉슨, 서로 다른 프로그램 켜서 놓고 본다는 것입니다.
만약에 인터넷 통신을 하고 있다면 모를까, 이들간 통신은 쉬운게 아닙니다. 때문에 이런 데이터 참조간에
지연이 발생합니다. 만약에 이런 통신을 무시하고 돌리게 되면 어떻게 될까요?
"""

GLOBAL_VAR_4 = 0


def add_one_3():
    global GLOBAL_VAR_4
    for i in range(1000000):
        GLOBAL_VAR_4 += 1


if __name__ == "__main__":
    start = time.time()
    pr_1 = Process(target=add_one_3)
    pr_2 = Process(target=add_one_3)
    pr_1.start()
    pr_2.start()
    pr_1.join()
    pr_2.join()
    # print(GLOBAL_VAR_4)  # 종료 후 변수의 값 확인
    # print(time.time() - start)
"""
시간이 개선됬는지야 잘 모르지만, 중요한건 값이 전혀 증가하지 않았다는 것입니다. Global문제도 아닙니다.
이건 별개의 프로그램으로서 작동했기 때문에 그렇습니다.
때문에 이런 문제의 경우에는 아래와 같이 하는 것이 효율적입니다.
"""


def add_one_4(que: Queue):
    n = 0
    for i in range(1000000):
        n += 1
    que.put(n)


if __name__ == "__main__":
    q = Queue()
    start = time.time()
    pr_1 = Process(target=add_one_4, args=(q, ))
    pr_2 = Process(target=add_one_4, args=(q, ))
    pr_1.start()
    pr_2.start()
    pr_1.join()
    pr_2.join()
    VAR_1 = q.get() + q.get()
    # print(VAR_1)
    # print(time.time() - start)
"""
기존 multithread나 한개의 thread로 돌린 것과는 다르게 시간이 많이 개선되었음을 알게되었습니다.
모든 경우에 이럴까요?
"""


def add_one_5(que: Queue):
    n = 0
    for i in range(10):
        n += 1
    que.put(n)


if __name__ == "__main__":
    q = Queue()
    start = time.time()
    pr_1 = Process(target=add_one_5, args=(q, ))
    pr_2 = Process(target=add_one_5, args=(q, ))
    pr_1.start()
    pr_2.start()
    pr_1.join()
    pr_2.join()
    VAR_2 = q.get() + q.get()
    print(VAR_2)
    print(time.time() - start)
"""
아까와 다르게 수가 확 줄었음에도 시간이 극적으로 개선되지 않았습니다. 이는 각 Process에서 값을 보내고,
다시 가져오는 과정 자체가 난이도가 높아서 생기는 문제입니다. 연산 자체가 문제가 아니라는 것입니다.
결국 적은 횟수에 대해서는 오히려 단일 thread나 multithread가 나은 것입니다.
"""

"""
이들을 고려하더라도 무한대의 thread나 process는 컴퓨터 파워가 허락치 않으면 작동하지 않습니다. 컴퓨터의
cpu의 연산을 넘어서는 개수의 thread나 process가 발생할 경우에는 당연히 병목현상이 발생하면서 전체적으로
느려지게 되는 것입니다. 이 또한 개발자가 신경쓰고 관리해야할 것입니다.
전체적인 느려짐을 제공할 것이냐, 제한적인 인원에 대해서 빠르게 처리하고 다음을 처리하게 만들것이냐.
이런 고민을 하게 될 것입니다.
"""

