#!/bin/bash
set -euxo pipefail
WORKDIR=$(pwd)
cd "$(dirname "$0")"

cd downloads
curl -O http://bigg.ucsd.edu/static/namespace/bigg_models_reactions.txt
curl -O http://bigg.ucsd.edu/static/namespace/bigg_models_metabolites.txt
