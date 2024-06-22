{
  #setting urls to pull from
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable"; 
  inputs.poetry2nix.url = "github:nix-community/poetry2nix";

  outputs = { self, nixpkgs, poetry2nix }: 
    let
      supportedSystems = [ "x86_64-linux" "x86_64-darwin" "aarch64-linux" "aarch64-darwin" ];
      forAllSystems = nixpkgs.lib.genAttrs supportedSystems;
      allPkgs = forAllSystems (system: nixpkgs.legacyPackages.${system});
    in
    {

      #Turn the poetry.lock into a package for nix
      packages = forAllSystems (system: let
        pkgs =  allPkgs.${system};
        themeSet = {
          "jsonresume-theme-full" = {
            owner   = "jackkeller";
            version = "unstable-2023-07-16";
            rev     = "66e3d0673db9b436e4fb7cdf5d9dc336d1f3a0a4";
            hash    = "sha256-ZYAExajB2BUXf17fOYnLFEZAeKCnCnjwym/VO1k2yk8=";
            npmHash = "sha256-jqsrQaMth71kGk6NEyGgUbjVHhpXn2kIDi/T6tmbcZI=";
          };
          "jsonresume-theme-fullmoon" = {
            owner   = "IsFilimonov";
            version = "0.1.2";
            rev     = "v0.1.2";
            hash    = "sha256-6zdqIE/DpuLhlQ6OFrOfNGu7Vq8w+0OAcMYCNQXD1xY=";
            npmHash = "sha256-1DIxCiUWF46YSCjvIzrXwz0w6+TwdXndUgb0Pgd3kHI=";
          };
        };
        inherit (poetry2nix.lib.mkPoetry2Nix { inherit pkgs; }) mkPoetryApplication;
      in {
        default = mkPoetryApplication { projectDir = self; };
        runResumed = pkgs.writeShellScriptBin "resumed-wrap" ''
          ${pkgs.resumed}/bin/resumed render --theme \
            ${self.packages.${system}.themes}/lib/node_modules/$1/index.js  
        '';

        themes = let 
          themeList = builtins.attrValues themePkgs;
          themePkgs = pkgs.lib.mapAttrs (pname: value: 
            pkgs.buildNpmPackage {
              inherit pname;
              inherit (value) version;
              
              src = pkgs.fetchFromGitHub {
                inherit (value) rev hash owner;
                repo = pname;
              };
    
              npmDepsHash = value.npmHash;
              dontNpmBuild = true;
            }
          ) themeSet;
        in pkgs.symlinkJoin {name = "json-resume-theme-pkgs"; paths = themeList;};
      });

      #creates shell env
      devShells = forAllSystems (system: let
        pkgs = allPkgs.${system};
        inherit (poetry2nix.lib.mkPoetry2Nix { pkgs = pkgs; }) mkPoetryEnv;
      in {
        default = pkgs.mkShellNoCC {
          packages = with pkgs; [
            (mkPoetryEnv { projectDir = self; })
            poetry
            resumed
          ];
        };
      });
    };
}
