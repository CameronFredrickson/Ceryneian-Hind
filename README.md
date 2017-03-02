# Ceryneian-Hind
A script to get the locations of users from the 42 api given a user's id.
1. Create an application [here](https://profile.intra.42.fr/oauth/applications/new).
2. Once your application is created enter the UID and SECRET keys in your shell like this:
~~~
export CLIENT_ID=YOUR_UID_KEY
export SECRET=YOUR_SECRET_KEY
~~~
3. Reload your bash profile by running `source./bash_profile` or run `zsh .zshrc` if you are using zsh.
4. add the usernames you wish to query from the api to the users text file or create your own.
5. Run the script `python ceryneian_hind.py users`
