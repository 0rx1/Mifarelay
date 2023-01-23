import subprocess

def choose_uid():
    with open('UIDs.txt', 'r') as f:
        uids = f.readlines()
        for i, uid in enumerate(uids):
            print(f'{i+1}. {uid.strip()}')
        choice = int(input('Which UID would you like to use? Please enter the number corresponding to the UID: '))
        selected_uid = uids[choice-1].strip()
        subprocess.run(f'pm3 -c hf 14a sim -t 1 --uid {selected_uid}', shell=True)

choose_uid()
