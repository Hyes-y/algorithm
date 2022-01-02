def solution(genres, plays):
    answer = []
    check_dict = {genre: 0 for genre in set(genres)}
    check_index = {genre: [] for genre in set(genres)}

    for i in range(len(genres)):
        check_dict[genres[i]] += plays[i]
        check_index[genres[i]].append((i, plays[i]))

    genres_rank = list(check_dict.items())
    genres_rank = sorted(genres_rank, key=lambda x: x[1], reverse=True)

    while len(answer) < 4:
        for i in range(len(genres_rank)):
            most_play = check_index[genres_rank[i][0]]
            most_play.sort(key=lambda x: x[1], reverse=True)
            answer.append(most_play[0][0])
            if len(most_play) >= 2:
                answer.append(most_play[1][0])

    return answer


genres=["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]

solution(genres, plays)