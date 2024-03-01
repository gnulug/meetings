let
  pkgs = import <nixpkgs> {};
in pkgs.dockerTools.buildLayeredImage {
  name = "my-image";
  tag = "latest2";
  config.Cmd = [ "${pkgs.bashInteractive}/bin/bash" ];
  contents = [
  ];
}
