import os
import jsonlines as jl

END_FILE_TAGS = ["FADE OUT.", "THE END"]

def add_corpus(session, member, corpus):
    """

    :param session:
    :param member:
    :param corpus:
    :return:
    """
    corpus = corpus.replace('\n', '')
    if member == '' or corpus == '': return session

    session.append(f"{member}: {corpus}")
    return session

def writer_session(writer, session):
    """

    :param writer:
    :param session:
    :return:
    """
    if len(session) > 1:
        writer.write(session)

def main(root_path):
    all_files = []
    for file in os.listdir(root_path):
        all_files.append(f"{root_path}/"+file)

    writer = jl.open(f"Star_Trek_{root_path}.jsonl", "w")

    for file_path in all_files:
        print(file_path)
        if not file_path.endswith('.txt'): continue

        # writer = jl.open(file_path + "_Star_Trek_The_Movies.jsonl", "w")

        start_TAG = False
        with open(file_path, "r") as f:
            # data = f.read()
            # code_res = chardet.detect(data)
            # if code_res['encoding'] != 'ascii': continue
            lines = f.readlines()
            # print(len(lines))
            session = []
            member = "BGM"
            corpus = ''
            for idx, line in enumerate(lines):
                line = line.strip()
                if line == '\n' or line == '':
                    session = add_corpus(session, member, corpus)
                    corpus = ''
                    member = 'BGM'
                    continue
                if line.startswith('('): continue
                if line.startswith('-'): continue
                if '/' in line and '-' in line: continue
                if line in END_FILE_TAGS: continue
                head, tail = line.split(' ')[0], ''.join(line.split(' ')[1:])
                if head.isdigit() and tail.isupper():
                    session = add_corpus(session, member, corpus)
                    writer_session(writer, session.copy())
                    start_TAG = True
                    session.clear()
                    corpus = ''
                    member = 'BGM'
                    continue

                if not start_TAG: continue
                if line.isupper():
                    session = add_corpus(session, member, corpus)
                    corpus = ''
                    member = line
                    continue
                if line != '':
                    corpus = corpus + line.replace('\n', '') + ' '
                # print(line)

    writer.close()

if __name__ == '__main__':
    root_path_list = ["scripts_mov", "scripts_tng", "scripts_ds9"]
    for root_path in root_path_list:
        main(root_path)
