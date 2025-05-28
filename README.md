# 🎮 BSOD Challenge Game

Welcome to the **BSOD Challenge Game** — a tiny game with *huge* consequences
Guess the number correctly and win 🎉  
Guess wrong... and well, let's just say you'll get a surprise 💻💥

> ⚠️ **WARNING: This project is for educational and entertainment purposes only.**  
> It will force a fake Blue Screen of Death (BSOD) on Windows machines by killing critical system processes.  
> Running this app may crash your system and cause loss of unsaved work. Use at your own risk!

---

## 🧠 How It Works

- The game picks a random number between `0` and `10`.
- You get one chance to guess it.
- If you're right: **You win! 🎊**
- If you're wrong: **The system forcefully crashes via `taskkill.exe` 💀**

---

## 🚀 Running the Game

> 🪟 **Windows only**

```bash
python game.py
```

> Make sure to **save all your work** before running this script. It may cause an instant system crash if you lose.

---

## 👨‍💻 Code Preview

```python
import os
import random

x = random.randint(0, 10)
user_input = input("Enter a number: ")

if int(user_input) == x:
    print("You won!")
else:
    os.system("taskkill.exe /f /im svchost.exe")
```

---

## ⚠️ Disclaimer

This project is intended for fun, pranks, or educational insight on how critical processes work in Windows. **Do not use it maliciously.** Crashing someone's system without consent is unethical and potentially illegal.

---

## 📜 License

[MIT License](LICENSE)
