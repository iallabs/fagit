if __name__ == "__main__":

    assert __git_version() == 0
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', type=str, default=DEFAULT)
    parser.add_argument('-o', '--organisation', type=str, default=_ORGANISATION)
    parser.add_argument('-p', '--private', action="store_true", default=False)
    parser.add_argument('-v', '--verbose', action="store_true", default=False)
    parser.add_argument('-c', '--clone', type=str)
    parser.add_argument('-b', '--build', type=str)
    parser.add_argument('-bo', '--build-option', type=str, default='')
    parser.add_argument('-m', '--make', type=str)
    args = parser.parse_args()

    if args.clone:
        clone_package(args.clone,
                      organisation=args.organisation,
                      private=args.private,
                      directory=args.directory,
                      verbose=args.verbose)
    if args.build:
        build_package(args.build,
                      build_option=args.build_option,
                      directory=args.directory)
    if args.make:
        __make_babtu_cfg(args.make,
                         target_dir=args.directory,
                         verbose=args.verbose)
