import sys
import io
from os import listdir
from os.path import isfile, join
from response import my_response

tests_path = "tests"
onlyfiles = ["{}/{}".format(tests_path, f) for f in listdir(tests_path) if isfile(join(tests_path, f))]
inputs = []
outputs = []

for file in onlyfiles:
    if "input" in file:
        inputs.append(file)
    elif "output" in file:
        outputs.append(file)
inputs.sort()
outputs.sort()
count = 0

for input_test, output_test in zip(inputs, outputs):
    try:
        f_input = open(input_test, "r")
        f_output = open(output_test, "r")
        out = f_output.readline()
        lines = []
        for x in f_input:
            lines.append(x.replace('\n', ''))

        print("\033[1;32;40m ---------------------INPUT------------------------------\033[0m")
        print(lines)

        print("\033[1;34;40m---------------------EXPECTED RESPONSE------------------------------\033[0m")
        print(out)

        text_trap = io.StringIO()
        sys.stdout = text_trap
        rep = my_response(lines=lines)
        if str(rep) != str(out):
            sys.stdout = sys.__stdout__
            print("\033[1;31;40m---------------------WRONG ANSWER------------------------------\033[0m")
        else:
            sys.stdout = sys.__stdout__
            print("\033[1;32;40m ---------------------GOOD ANSWER------------------------------\033[0m")
            count = count + 1

        my_response(lines)
        print("*----------------------------------------------------------------------------------------------------*\n"
              )
    except Exception as e:
        f_input.close()
        f_output.close()
        print(e)
        break

if count == len(inputs):
    print("\033[1;32;40m {}/{} \033[0m".format(count, len(inputs)))
else:
    print("\033[1;31;40m {}/{} \033[0m".format(count, len(inputs)))
