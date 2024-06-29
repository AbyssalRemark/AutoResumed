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
    packages = forAllSystems (system: 
    let
      pkgs =  allPkgs.${system};
      
      #add theme data to this file
      themeSet = pkgs.lib.importJSON ./themes.json; 
      
      #Turn the poetry.lock into a package for nix
      inherit (poetry2nix.lib.mkPoetry2Nix { inherit pkgs; }) mkPoetryApplication;
    in {
      default = mkPoetryApplication { projectDir = self; };
      #creates shell script to execute Resumed
      runResumed = pkgs.writeShellScriptBin "resumed-wrap" ''
        JSON=''${1:-resume.json}
        THEME=''${2:-jsonresume-theme-macchiato-plus}
        ${pkgs.resumed}/bin/resumed render $JSON --theme \
          ${self.packages.${system}.themes}/lib/node_modules/$THEME/index.js  
      '';

      generatePdf = pkgs.callPackage ./tools/pdf-export {};

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
            
            #puppeteer is used for testing and is not needed and breaks things. 
            #This tells it to go away
            PUPPETEER_SKIP_CHROMIUM_DOWNLOAD = 1;

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
