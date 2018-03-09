import tensorflow as tf

state = tf.Variable(0, name="counter")#변수 초기화

one = tf.constant(1)#더할 변수 추가
newVal = tf.add(state, one)#더하기
update = tf.assign(state, newVal)#더한값을 반영

#initOperation = tf.initialize_all_variables() 은 없어졌음
initOperation = tf.global_variables_initializer()#init Operation, 오퍼레이션 초기화

with tf.Session() as sess:#그래프 생성, sess=tf.Session()과 같은의미
    sess.run(initOperation)#오퍼레이션 초기화
    print(sess.run(state))#처음값 출력, 0
    for i in range(3):
        sess.run(update)#+1한 값을 반영
        print(sess.run(state))#현재값 출력
