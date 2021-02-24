"""
m	musicinfos	answer
ABCDEFG	[12:00,12:14,HELLO,CDEFGAB, 13:00,13:05,WORLD,ABCDEF]	HELLO
CC#BCC#BCC#BCC#B	[03:00,03:30,FOO,CC#B, 04:00,04:08,BAR,CC#BCC#BCC#B]	FOO
ABC	[12:00,12:14,HELLO,C#DEFGAB, 13:00,13:05,WORLD,ABCDEF]	WORLD
각 음은 1분에 1개씩 재생된다.
"""
#[재생이 시작되고 끝난 시간 ,음악제목, 악보]
import pdb
def re_sharp(music):
    music = music.replace("C#","c")
    music = music.replace("A#","a")
    music = music.replace("D#","d")
    music = music.replace("F#","f")
    music = music.replace("G#","g")
    return music
def solution(m, musicinfos):
    success_list = []
    for idx,info in enumerate(musicinfos):
        new_note=""
        note = ""
        info_list = info.split(",")
        s_hour, s_min = info_list[0].split(':')
        e_hour, e_min = info_list[1].split(':')
        title = info_list[2]
        note = info_list[3]
        note = re_sharp(note)
        t_hour = int(e_hour)-int(s_hour)
        t_min = int(e_min) - int(s_min)
        t_min += 60 * t_hour
        
        new_note = note * (t_min//len(note)) 
        new_note = new_note + note[:(t_min%len(note))]
        m = re_sharp(m)

        # if new_note in m :
        #     success_list.append([idx,title, t_min])
            

        # if m in new_note:
        #     success_list.append([idx,title, t_min])
        """
        가장 중요한것    
        "" in anystring:
        True
        anystring in ""
        False
        """
        if m in new_note :
            success_list.append([idx,title, t_min])                
    success_list.sort(key=lambda x : (-x[2],x[0]))
    if success_list:
        return success_list[0][1]
    return "(None)"