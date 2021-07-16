from .start_connect import cur

class TagToPaper():
    def __init__(self, tags: list):
        self.tags = []
        for i in tags:
            self.tags.append(i[0])

    def tag_to_paper(self):
        papers_id = []
        q = """SELECT * FROM paper_tag WHERE 'id_tag' = ?;"""
        for cur_tag in self.tags:
            if isinstance(cur_tag, int):
                for i in cur.execute(q, [cur_tag]):
                    papers_id.append(i[0])
            else:
                for i in cur.execute(q, [cur_tag[0]]):
                    papers_id.append(i[0])

        papers = []
        q = """SELECT * FROM paper WHERE 'id' = ?;"""
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
        tags_id = []
        q = f"""SELECT * FROM paper_tag WHERE 'id_paper' = ?;"""
        for cur_paper in self.papers:
            if isinstance(cur_paper, int):
                for i in cur.execute(q, [cur_paper]):
                    tags_id.append(i[1])
            else:
                for i in cur.execute(q, [cur_paper[0]]):
                    tags_id.append(i[1])

        tags = []
        q = f"""SELECT * FROM tag WHERE 'id' = ?;"""
        for cur_tag_id in tags_id:
            for i in cur.execute(q, [cur_tag_id]):
                tags.append(i)

        return tags