# Given a set of strings that represent directories. Return a string representing
# the part of the directory tree that is common to all of the directoriess

directories = [
    '/home/jenny/code/search/common/',
    '/home/jenny/code/api/client',
    '/home/jenny/code/service/app/tests'
    ]

ouput = '/home/jenny/code'


def common_path(directories):
    directory_list = []
    # preprocess: split on "/"
    dir_tree = [x.split("/") for x in directories]

    # preprocess: get rid of empty strings
    for item in dir_tree:
        directory = [x for x in item if x]
        directory_list.append(directory)

    i = 0
    while i < len(directory_list[0]):
        for directory in directory_list:
            if directory[i] != directory_list[0][i]:
                return('/'.join(directory_list[0][:i]))
        i += 1
    return('/'.join(directory_list[0][:i]))


print(common_path(directories))