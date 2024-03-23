# ____ Greedy algorith ____

def base_process_sort_profit(d, p):
    prof_dead = dict()
    tasks  = [i for i in range(1, len(d)+1)]
    for i in tasks:
        prof_dead[i] = p[i-1]

    prof_dead = dict(sorted(prof_dead.items(), key=lambda item: item[1], reverse = True))
    return prof_dead

# ITERATIVE

def job_greedy_iter(d, p):
    prof_dead = base_process_sort_profit(d, p)
    schedule = [0 for _ in range(max(d))]

    for i in prof_dead:
        times = d[i-1]
        if schedule[times-1] == 0:
            schedule[times - 1] = prof_dead[i]
        else:
            for z in range(times):
                if schedule[z] == 0:
                    schedule[z] = prof_dead[i]
                    break

    return sum(schedule)

# RECURSIVE

def job_greedy_rec(d, p):
    prof_dead = base_process_sort_profit(d, p)
    p = [i for i in prof_dead.values()]
    d = [d[i-1] for i in prof_dead]
    schedule = [0 for _ in range(max(d))]
    return job_greedy_rec_helper(d, p, schedule, i=0)


def job_greedy_rec_helper(d, p, schedule, i):
    if i>len(schedule):
        return sum(schedule)
    if schedule[d[i]-1] == 0:
        schedule[d[i]-1] = p[i]
    else:
        for z in range(d[i]-2, -1, -1):
            if schedule[z] == 0:
                schedule[z] = p[i]
                break
    return job_greedy_rec_helper(d, p, schedule, i+1)


deadlines = [9, 2, 5, 7, 4, 2, 5, 7, 4, 3]
profit = [15, 2, 18, 1, 25, 20, 8, 10, 12, 5]

print("Greedy Algorithm Iterative:", job_greedy_iter(deadlines, profit))
print("Greedy Algorithm Recursive:", job_greedy_rec(deadlines, profit))



