import subprocess

class ProcessManager:

    def run_tool(self, command):

        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        output, error = process.communicate()

        return output.decode()