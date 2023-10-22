
# Getting info from GitHub REST API

Example usage GitHub REST API

* https://docs.github.com/en/rest
* https://docs.github.com/en/rest/overview/resources-in-the-rest-api
<br> <br>

### Example with curl:<br>
    * curl -L \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer <YOUR-TOKEN>" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    https://api.github.com/repos/OWNER/REPO/commits/REF
