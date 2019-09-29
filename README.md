# macOS Box

This is an Ansible role to help reproducibly setup macOS development systems.

## Requirements

This role has no special requirements beyond macOS and the dependencies listed
in `meta/main.yml`.

## Role Variables

At present, this role provides just two of its own variables while also
providing some very minimal default values for its dependencies.
Dependencies listed alphabetically. See `meta/main.yml` for execution
order.

Follow the links to individual roles' Galaxy pages for complete lists of
their variables.

### `ctorgalson.dotfiles` defaults

| Name             | Default | Description |
|------------------|---------|-------------|
| `dotfiles_repos` | `[]`    | "A list of dotfiles to clone and use to create dotfiles in the user directory." |

See: [ctorgalson.dotfiles](https://galaxy.ansible.com/ctorgalson/dotfiles)

### `ctorgalson.files` defaults

| Name          | Default | Description |
|---------------|---------|-------------|
| `files_files` | `[]`    | "a list of [file] objects using Ansible File module params." |

See: [ctorgalson.files](https://galaxy.ansible.com/ctorgalson/files)

### `ctorgalson.macosbox` (this role!) defaults

| Name       | Default | Description |
|------------|---------|-------------|
| `mb_user`  | `""`    | Convenience variable for use in other role variables. The name of the account the role is running to configure. **Required**. |
| `mb_group` | `staff` | Convenience variable for use in other role variables. The default group for files in the account. Should seldom need changing. |
| `mb_run_geerlingguy_mas` | `false` | Whether or not to run the `geerlingguy.mas` role (the role sometimes has trouble running over ssh connections, and won't run in a playbook using `become`). |

### `ctorgalson.ssh_keys` defaults

| Name                  | Default                 | Description |
|-----------------------|-------------------------|-------------|
| `ssh_user`            | `{{ mb_user }}`         | "Name of ssh key owner." |
| `ssh_user_home`       | `/Users/{{ ssh_user }}` | "Derived path to owner's home directory." |
| `ssh_ssh_dir_group`   | `{{ mb_group }}`        | "Group of .ssh directory." |
| `ssh_ssh_keys`        | `[]`                    | "List of ssh keys." |
| `ssh_authorized_keys` | `[]`                    | "List of paths to public keys to be added to authorized_keys file." |

See: [ctorgalson.ssh_keys](https://galaxy.ansible.com/ctorgalson/ssh_keys)

### `elliotweiser.osx-command-line-tools` defaults

None.

See: [elliotweiser-osx-cli-tools](https://galaxy.ansible.com/elliotweiser/osx-cli-tools)

### `geerlingguy.homebrew` defaults

| Name                            | Default | Description |
|---------------------------------|---------|-------------|
| `homebrew_cask_apps`            | `[]`    | "Apps you would like to have installed via `cask`." |
| `homebrew_installed_packages`   | `[]`    | "Packages you would like to make sure are installed via `brew install`. " |
| `homebrew_taps`                 | `[]`    | "Taps you would like to make sure Homebrew has tapped." |
| `homebrew_uninstalled_packages` | `[]`    | "Packages you would like to make sure are _uninstalled_." |

See: [geerlingguy.homebrew](https://galaxy.ansible.com/geerlingguy/homebrew)

### `geerlingguy.mas` defaults

Note that [`geerlingguy.mas` may not function correctly over ssh
connections](https://github.com/geerlingguy/ansible-role-mas/issues/7), and
is therefore disabled except when this role is running on a local connection.

| Name                 | Default | Description |
|----------------------|---------|-------------|
| `mas_installed_apps` | `[]`    | "A list of [app store] apps to ensure are installed on the computer." |

See: [geerlingguy.mas](https://galaxy.ansible.com/geerlingguy/mas)

## Dependencies

This role relies on a series of other Galaxy roles (mostly mine at
present).

_This_ role only sets enough defaults to test with. Some, all, many, or
none of the variables available to the other roles may need to be set to
create a useful build for your purposes, so please consult the READMEs for
the other roles to find out what variables they make available:

- [ctorgalson.dotfiles](https://galaxy.ansible.com/ctorgalson/dotfiles)
- [ctorgalson.files](https://galaxy.ansible.com/ctorgalson/files)
- [ctorgalson.macos_hostname](https://galaxy.ansible.com/ctorgalson/macos_hostname)
- [ctorgalson.ssh_keys](https://galaxy.ansible.com/ctorgalson/ssh_keys)
- [elliotweiser-osx-cli-tools](https://galaxy.ansible.com/elliotweiser/osx-cli-tools)
- [geerlingguy.homebrew](https://galaxy.ansible.com/geerlingguy/homebrew)
- [geerlingguy.mas](https://galaxy.ansible.com/geerlingguy/mas)

To see an example playbook, please see `tests/provision.yml`, and the
contents of `tests/group_vars/`. The file `tests/test.py` may also be
useful as a way of determining what results the provision playbook aims
to achieve.

## Example Playbook

    - hosts: servers
      roles:
         - ansible-role-macosbox
      vars:
        # elliotweiser.osx-command-line-tools vars.
        # (None required)

        # ctorgalson.dotfiles vars.
        dotfiles_repos:
          - repo: "https://git@github.com/paulirish/dotfiles.git"
            owner: "macosbox"
            group: "staff"
            name: "dotfiles"
            version: "master"
            whitelist:
              - ".gitconfig"
              - ".vimrc"

        # ctorgalson.files vars.
        files_files:
          - path: "/Users/macosbox/Dev"
            state: directory
            owner: "macosbox"
            group: "staff"

        # ctorgalson.macos_hostname vars.
        mh_localhostname: "MacOsBox"
        mh_computername: "macOS Box"

        # ctorgalson.ssh_keys vars.
        ssh_user: "macosbox"
        ssh_user_home: "/Users/macosbox"
        ssh_ssh_dir_group: "staff"
        ssh_ssh_keys:
          - src: "files/keys/id_rsa"
          - src: "files/keys/id_rsa.pub"
        ssh_public_key_mode: "0644"
        ssh_authorized_keys:
          - "files/keys/authorized/id_rsa.pub"

        # elliotweiser.osx-cli-tools vars.

        # geerlingguy.homebrew vars.
        homebrew_cask_apps:
          - "firefox"
          - "iterm2"
        homebrew_installed_packages:
          - "composer"
          - "mas"
          - "node@10"
          - "php"

        # geerlingguy.mas vars.
        - id: "409183694"
          name: "Keynote (9.1)"

## License

GPLv3

## Author Information

Christopher Torgalson
