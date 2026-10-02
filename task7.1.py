import sched, time

s = sched.scheduler(time.time, time.sleep)

def say(text):
    print(f"[{time.strftime('%H:%M:%S')}] {text}")

start = time.time()
print("Start. Otschet vremeni ot t0 = 0\n")

s.enter(2, 1, say, ("Proshlo 2 sekundy (prioritet 1)",))
s.enter(2, 0, say, ("Proshlo 2 sekundy (prioritet 0 - srabotaet PERVYM)",))
s.enter(1, 1, say, ("Proshla 1 sekunda",))
s.enterabs(start + 3, 1, say, ("Absolyutnoe vremya t0+3 s",))
s.enter(0.5, 1, say, ("Proshlo 0.5 sekundy",))

print("Ochered do run():", len(s.queue), "zadach")
print("run() blokiruet potok, poka vse zadachi ne vypolnyatsya:\n")

s.run()

print("\nGotovo. Pustaya ochered?", s.empty())


#даже если время одинаковое, модуль sched будет смотреть на приоритетность задач. приор 0 выведется раньше чем приор 2
