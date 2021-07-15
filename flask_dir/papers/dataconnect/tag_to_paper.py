from .__init__ import cur

def tag_to_paper(tags: list):
    col_1 = 'id_tag'
    papers_id = []
    q = f"""SELECT * FROM paper_tag WHERE {col_1} = ?;"""
    for cur_tag in tags:
        tag_id = cur_tag[0]
        for i in cur.execute(q, (tag_id, )):
            papers_id.append(i[0])

    col_2 = 'id'
    papers = []
    q = f"""SELECT * FROM paper WHERE {col_2} = ?;"""
    for cur_paper_id in papers_id:
        for i in cur.execute(q, (cur_paper_id, )):
            papers.append(i)

    return papers