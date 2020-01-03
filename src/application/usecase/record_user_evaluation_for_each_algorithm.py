from src.adapters.gateway.user_evaluations.push_user_evaluations import push_user_evaluations


def record_user_evaluation_for_each_algorithm(user_id, user_evaluations):
    for algo_name in user_evaluations:
        push_user_evaluations(user_id, algo_name,
                              user_evaluations[algo_name]['text'], user_evaluations[algo_name]['evaluation_id'])
