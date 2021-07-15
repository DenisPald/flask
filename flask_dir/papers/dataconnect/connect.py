from .__init__ import cur

def tag_to_paper(tags: list):
    col_1 = 'id_tag'
    papers_id = []
    q = f"""SELECT * FROM paper_tag WHERE {col_1} = ?;"""
    for cur_tag in tags:
        for i in cur.execute(q, (cur_tag, )):
            papers_id.append(i[0])

    col_2 = 'id'
    papers = []
    q = f"""SELECT * FROM paper WHERE {col_2} = ?;"""
    for cur_paper_id in papers_id:
        for i in cur.execute(q, (cur_paper_id, )):
            papers.append(i)

    return papers


def paper_to_tag(papers: list):
    col_1 = 'id_paper'
    tags_id = []
    q = f"""SELECT * FROM paper_tag WHERE {col_1} = ?;"""
    for current_paper in papers:
        for i in cur.execute(q, (current_paper, )):
            tags_id.append(i[1])

    col_2 = 'id'
    tags = []
    q = f"""SELECT * FROM tag WHERE {col_2} = ?;"""
    for cur_tag_id in tags_id:
        for i in cur.execute(q, (cur_tag_id, )):
            tags.append(i)

    return tags