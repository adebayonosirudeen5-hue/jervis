import subprocess

class CommandExecutor:
    def execute_command(self, command):
        """Executes a shell command and returns the output"""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout
            else:
                return result.stderr
        except Exception as e:
            return str(e)

# Example usage
if __name__ == '__main__':
    executor = CommandExecutor()
    output = executor.execute_command('echo Hello, World!')
    print(output)
