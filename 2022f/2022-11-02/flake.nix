{
  description = "Flake utils demo";

  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let pkgs = nixpkgs.legacyPackages.${system}; in
      {
        devShells = {
          default = pkgs.mkShell {
            buildInputs = [
              pkgs.rr
              pkgs.cde
              pkgs.strace
              pkgs.ncurses6
              pkgs.ncurses6.dev
              pkgs.grub2
              pkgs.xorriso
              pkgs.qemu
            ];
            shellHook = ''
              export C_INCLUDE_PATH=:$C_INCLUDE_PATH
              export HOSTCFLAGS="-I${pkgs.ncurses6.dev}/include"
              export HOSTLDFLAGS="-L${pkgs.ncurses6}/lib -lncursesw"
            '';
          };
        };
      }
    );
}
