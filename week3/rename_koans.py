#!/bin/bash
import md5, argparse, os


class FileToMd5Script(object):

    def __init__(self):
        self.parse_arguments()
        self.join_full_file_path()
        self.compute_file_md5_hex()
        print self.md5sum

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description="Processes file_name")
        parser.add_argument("file_name", help='name of the file to take md5')
        parser.add_argument("--file_path", help='directory path of file')
        self.args = parser.parse_args()

    def join_full_file_path(self):
        args = self.args
        if args.file_path:
            self.full_file_path = os.path.join(args.file_path, args.file_name)
        else:
            self.full_file_path = args.file_name

    def compute_file_md5_hex(self):
        with open(self.full_file_path, 'r') as md5_to_get:
            file_data = md5_to_get.read()
            md5sum = md5.new()
            md5sum.update(file_data)
            self.md5sum = md5sum.hexdigest()

if __name__ == "__main__":
    FileToMd5Script()


#echo "Zipping"
#zip -r python_koans.zip python_koans
#
#curr_koans=${1:-$(ls python_koans-*)}
#echo "Current koans is: " $curr_koans
#
#next_koans="python_koans-$(md5 python_koans.zip | awk -F " = " '{ print $2 }' | cut -c 1-8)".zip
#echo "Next koans is: " $next_koans
#
#echo "Moving current to next"
#mv python_koans.zip $next_koans
#
#echo "Replacing current with next in wiki"
#sed -i -e "s/$curr_koans/$next_koans/" ../../eca201.wiki/setup_python_koans.rest
#
#echo "Verifying grep"
#grep -q $next_koans ../../eca201.wiki/setup_python_koans.rest || echo "failed"
#
#rm $curr_koans
