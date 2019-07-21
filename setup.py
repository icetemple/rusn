from setuptools import setup


with open('README.md', 'r') as f:
    readme = f.read()


if __name__ == '__main__':
    setup(
        name='rusn',
        version='1.0.1',
        author='Dmitriy Pleshevskiy',
        author_email='dmitriy@ideascup.me',
        description='Small library for getting russian text with singular and plural forms',
        long_description=readme,
        long_description_content_type='text/markdown',
        package_data={'': ['LICENSE', 'README.md']},
        include_package_data=True,
        license='MIT',
        packages=['rusn']
    )
