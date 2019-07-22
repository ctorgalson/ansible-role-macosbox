# macOS Box

This is an Ansible role to help reproducibly setup macOS development systems.

## Requirements

Any pre-requisites that may not be covered by Ansible itself or the role should
be mentioned here. For instance, if the role uses the EC2 module, it may be a
good idea to mention in this section that the boto package is required.

## Role Variables

At present, this role provides just two of its own variables while also
providing some very minimal default values for its dependencies.

### `elliotweiser.osx-command-line-tools` defaults.

None.

### `ctorgalson.macosbox` (this role!) defaults

| Name       | Default | Description |
|------------|---------|-------------|
| `mb_user`  | `""`    | Convenience variable for use in other role variables. The name of the account the role is running to configure. **Required**. |
| `mb_group` | `staff` | Convenience variable for use in other role variables. The default group for files in the account. Should seldom need changing. |

### `ctorgalson.files` defaults

| Name | Default | Description |
|----------------|-------------|-------------|
| `files_files`  | `[]`        | List of files, links, and directories to create or copy to the machine. |

### `ctorgalson.dotfiles` defaults

| Name | Default | Description |
|------|---------|-------------|
| `dotfiles_repos` | `[]` | List of dotfiles repositories to clone. |

### `ctorgalson.ssh_keys` defaults

| Name                  | Default                 | Description |
|-----------------------|-------------------------|-------------|
| `ssh_user`            | `{{ mb_user }}`         | Account owner. Used to set paths and ownership of files and directories. |
| `ssh_user_home`       | `/Users/{{ ssh_user }}` | User home directory. |
| `ssh_ssh_dir_group`   | `{{ mb_group }}`        | Group for .ssh directory. |
| `ssh_ssh_keys`        | `[]`                    | List of ssh keys. |
| `ssh_authorized_keys` | `[]`                    | List of public ssh keys whose contents should be appended to the `authorized_keys` file. |

See the links in the Dependencies section, below, for complete lists of
variables that can be used by the dependent roles.

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

## License

GPLv3

## Author Information

Christopher Torgalson
