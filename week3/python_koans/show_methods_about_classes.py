from koans.about_classes import AboutClasses

for method in dir(AboutClasses):
    if 'test_' in method:
        print method
