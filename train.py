from states import *
import numpy as np

Q = np.array(np.zeros([MATRIX_SIZE, MATRIX_SIZE]))

# learning parameter
gamma = 0.1

initial_state = 3


def available_actions(state):

    current_state_row = R[state, :]
    av_act = np.where(current_state_row >= 0)[0]
    return av_act


available_act = available_actions(initial_state)


def sample_next_action(available_actions_range):
    next_action = int(np.random.choice(available_actions_range, 1))
    return next_action


action = sample_next_action(available_act)


def update(current_state, action, gamma):
    max_index = np.where(Q[action,] == np.max(Q[action,]))[0]

    if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size=1))
    else:
        max_index = int(max_index)
    max_value = Q[action, max_index]

    Q[current_state, action] = R[current_state, action] + gamma * max_value
    #print('max_value', R[current_state, action] + gamma * max_value)

    if np.max(Q) > 0:
        return np.sum(Q / np.max(Q) * 100)
    else:
        return 0


update(initial_state, action, gamma)



# Training
scores = []
for i in range(700):
    current_state = np.random.randint(0, int(Q.shape[0]))
    available_act = available_actions(current_state)
    action = sample_next_action(available_act)
    score = update(current_state,action,gamma)
    scores.append(score)
    print('Score:', str(score))

plt.plot(scores)
plt.show()
#print("Trained Q matrix:")
#print(Q/np.max(Q)*100)