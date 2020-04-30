from git import Repo
import logging
import time


logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO,
                    filename=u'./moxa_ports_git_push.log')
                    # filename=u'/var/log/SCRIPTS/moxa_ports_git_push.log')


def git_push(file_list, commit_message):
    repo = Repo('.')
    for file in file_list:
        repo.index.add(file)
    repo.index.commit(commit_message)
    origin = repo.remotes.origin
    try:
        origin.pull()
        origin.push(clone.refs.master)
    except Exception as error:
        logging.error('pull or push failed: {}'.format(error))
        time.sleep(300)
        git_push(file_list, commit_message)

