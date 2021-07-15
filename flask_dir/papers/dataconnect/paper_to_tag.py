from .__init__ import cur

def paper_to_tag(papers: list):
    col_1 = 'id_paper'
    tags_id = []
    q = f"""SELECT * FROM paper_tag WHERE {col_1} = ?;"""
    for current_paper in papers:
        paper_id = current_paper[0]
        for i in cur.execute(q, (paper_id, )):
            tags_id.append(i[1])

    col_2 = 'id'
    tags = []
    q = f"""SELECT * FROM tag WHERE {col_2} = ?;"""
    for cur_tag_id in tags_id:
        for i in cur.execute(q, (cur_tag_id, )):
            tags.append(i)

    return tags