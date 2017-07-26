import json
import subprocess


class LdeployParser:
    def __init__(self):
        # Open json file
        with open('ldeploy.json') as ldeploy_file:
            conf_json = json.load(ldeploy_file)

        self.conf_json = conf_json
        self.project_dir = conf_json['project_dir']

        # Construct ignore array
        self.ignore = []
        for item in conf_json["ignore"]:
            self.ignore.append("--exclude={}".format(item))

    def get_server(self, server):
        return self.conf_json["remote"][server]

    def rsync(self, conf):
        break_string = ["rsync", "-avz", "--chown={}".format(conf["chown"]), '-e "ssh -p {}"'.format(conf["port"]), "{}".format(self.project_dir)] + self.ignore + ["{}@{}:{}".format(conf["user"], conf["address"], conf["deploy_dir"])]
        execute_string = " ".join(break_string)
        subprocess.call(execute_string, shell=True)

    def ssh(self, conf):
        break_string = ["ssh", "-p {}".format(conf["port"]), "{}@{}".format(conf["user"], conf["address"])]
        execute_string = " ".join(break_string)
        subprocess.call(execute_string, shell=True)
