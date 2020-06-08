"""
베스트앨범

1. 속한 노래가 많은 장르부터
2. 장르 안에서 재생이 많이된 노래부터
3. 고유번호가 낮은 순서부터
4. 두개씩

알고리즘: 해쉬

1. 장르별로 노래를 담는다. (재생횟수, -고유번호)
2. 장르별로 속한 노래가 많은 순으로 sort
3. 장르안에서 솔팅을 하면 오래 걸리니깐 max를 두번하자.
"""


def solution(genres, plays):
    answer = []
    genres_dict, genres_sum = {}, {}
    for i, (genre, times) in enumerate(zip(genres, plays)):
        if genre in genres_dict:
            genres_dict[genre].append((times, -i))
            genres_sum[genre] += times
        else:
            genres_dict[genre] = [(times, -i)]
            genres_sum[genre] = times

    genres_num = []
    for genre in genres_dict:
        genres_num.append((genres_sum[genre], genre))
    genres_num.sort(reverse=True)

    for _, genre in genres_num:
        now_list = genres_dict[genre]
        if len(now_list) == 1:
            answer.append(-now_list[0][1])
        else:
            for _ in range(2):
                max_song = max(now_list)
                answer.append(-max_song[1])
                now_list.remove(max_song)

    return answer

