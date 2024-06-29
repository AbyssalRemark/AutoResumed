{buildNpmPackage, chromium, python3}:
buildNpmPackage (let
  version = "v0.1.0";
in {
  inherit version;
  src = ./.;
  nativeBuildInputs = [python3];
  pname = "html-pdf-export";
  PUPPETEER_SKIP_CHROMIUM_DOWNLOAD = 1;
  npmDepsHash = "sha256-DC9f++84BPNX6UoTSK8ZPJNDBIPbodbmBqoKyPr9ZiE=";
  dontNpmBuild = true;
  postInstall = ''
    wrapProgram $out/bin/html-pdf-export \
      --set PUPPETEER_EXECUTABLE_PATH ${chromium}/bin/chromium
  '';
})
