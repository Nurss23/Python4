# В посте были удалены некоторые комментарии, но был не тронут в том числе и последний
# Найти список удалённых комментариев

my_post = {
    "post": {
        "name": "Python",
        "comments": [
            {
                "id": 1,
                "text": "ok, that's good",
            },
            {
                "id": 7,
                "text": "checkout this",
            },
           {
                "id": 10,
                "text": "not bad",
            },
        ]
    }, 
    "userId": 1,
    "id": 1,
}
# Вывод:
# [2, 3, 4, 5, 6, 8, 9]