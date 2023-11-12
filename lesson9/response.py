my_post = {
    "post" : {
        "name": "python",
        "comments": [
            {
                "id" : "1",
                "text" : "ok, thats good",
            },
            {
                "id" : "6",
                "text" : "not bad",
            },
        ]
    },
    "useerid": 1,
    "id": 1,
}
comments_list = []
# print(my_post["post"] ["name"])
# print(["post"]["comments"][0]["text"]["text"])
for com in(["post"],["comments"]):
    comments_list.append(com["text"])
print(comments_list)