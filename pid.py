from gpiozero import RotaryEncoder
from simple_pid import PID
import time

CPR = ...  # counts per wheel rev
enc = RotaryEncoder(a=..., b=..., max_steps=0)
pid = PID(Kp, Ki, Kd, setpoint=1.0)  # rev/s
pid.output_limits = (0, 1)           # PWM duty
prev, t0 = enc.steps, time.monotonic()
while True:
    time.sleep(0.05)
    now = time.monotonic()
    speed = (enc.steps - prev) / (CPR * (now - t0))
    prev, t0 = enc.steps, now
    motor.value = pid(speed)
