from ModelClassifier import ModelClassifier


def main():
    temp_list = []
    test_model = ModelClassifier('C:/Users/Public/scans/Cube_Test02_BoxSize_Small(0).obj')
    hist_data = test_model.generate_distribution_data(test_model.plyObject.vertices)
    with open("training_data.txt", 'w') as training_data:
        temp_list.append(['Cube', hist_data[0], hist_data[1]])
        for line in temp_list:
            object_data = "{0}; {1}; {2}".format(line[0], list(line[1]), list(line[2]))
            training_data.write(object_data)


if __name__ == '__main__':
    main()
