from .start_connect import cur

class TagToPaper():
    def __init__(self, tags: list):
        self.tags = []
        for i in tags:
            self.tags.append(i[0])

    def tag_to_paper(self):
        col_1 = 'id_tag'
        papers_id = []
        q = f"""SELECT * FROM paper_tag WHERE {col_1} = ?;"""
        for cur_tag in self.tags:
            if isinstance(cur_tag, int):
                for i in cur.execute(q, [cur_tag]):
                    papers_id.append(i[0])
            else:
                for i in cur.execute(q, [cur_tag[0]]):
                    papers_id.append(i[0])

        col_2 = 'id'
        papers = []
        q = f"""SELECT * FROM paper WHERE {col_2} = ?;"""
        for cur_paper_id in papers_id:
            for i in cur.execute(q, [cur_paper_id]):
                papers.append(i)

        return papers

class PaperToTag():
    def __init__(self, papers: list):
        self.papers = []
        for i in papers:
            self.papers.append(i[0])

    def paper_to_tag(self):
        col_1 = 'id_paper'
        tags_id = []
        q = f"""SELECT * FROM paper_tag WHERE {col_1} = ?;"""
        for cur_paper in self.papers:
            if isinstance(cur_paper, int):
                for i in cur.execute(q, [cur_paper]):
                    tags_id.append(i[1])
            else:
                for i in cur.execute(q, [cur_paper[0]]):
                    tags_id.append(i[1])

        col_2 = 'id'
        tags = []
        q = f"""SELECT * FROM tag WHERE {col_2} = ?;"""
        for cur_tag_id in tags_id:
            for i in cur.execute(q, [cur_tag_id]):
                tags.append(i)

        return tags