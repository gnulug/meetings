{
  description = "Flake utils demo";

  inputs = {
    flake-utils = {
      url = "github:numtide/flake-utils";
    };
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let pkgs = nixpkgs.legacyPackages.${system}; in
      rec {
        # Use `nix develop` to get this shell.
        packages = {
          vanilla_fs = pkgs.stdenv.mkDerivation {
            name = "vanilla_fs";
            src = ./.;
            nativeBuildInputs = [
              pkgs.pkg-config
            ];
            propagatedBuildInputs = [
              pkgs.fuse3
            ];
            installPhase = ''
              mkdir -p $out/bin
              mv vanilla_fs $out/bin
            '';
          };
          default = packages.vanilla_fs;
        };
        app = {
          default = {
            program = "${packages.vanilla_fs}/bin/vanilla_fs";
            type = "app";
          };
        };
      }
    );
}
