from koans.about_asserts import AboutAsserts

for method in dir(AboutAsserts):
    if 'test_' in method:
        print method
