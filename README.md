# CVEoverview

Project to keep track of CVE's for both red and purple teams.
For now , this project uses the dataset of nist.gov as they supply an easy to parse and detailed dataset seperated in a logical manner.
In the future, a better candidate may be selected, but for now they offer (almost) everything we need to start this project.

# Main goals

Daily new CVE's are arising and will have an impact on both Blue and Red teams.
To reduce the time spend on learning every CVE, gathering the required information for your environment and to proces this information, CVEoverview will try to reduce the time spend on learning about CVE's and provide a detail overview with multiple modules.

CVEoverview can be seen as a framework which tries to accomplish x things:
- Bundle information into a single 'overview', combining multiple sources into one.
- Splitting the sources for Blue or Red teamers, meaning defensive meassures and offensive capabilities of that CVE can be seperated/optimized depending on the team.
- Reduce the time spend on all 'basic' searching when a new CVE appears, leaving more room to handle upon the actual CVE.

## Realised this far (PoC phase)
- Very basic implementation for collecting the files which are configured in config.yml and load the .json into memory.
- Thats is, processing data the actual data is wip now.

## TODO
- Create simple analytic overview
- Request data from multiple sources on the CVE (Published exploit on twitter ? Article on big website ? Other ways of news ?)

## Would be nice
- Decent front-end (Flask ?)
