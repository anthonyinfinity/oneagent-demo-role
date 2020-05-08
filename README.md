# This is a quick tutorial on TDD with Ansible & Molecule.

Requirements:

-   Docker
-   Ansible
-   Molecule.

## Getting started

Use molecule to bootstrap your ansible role.
`molecule init role oneagent-demo-role`

    ├── README.md
    ├── defaults
    │   └── main.yml
    ├── files
    ├── handlers
    │   └── main.yml
    ├── meta
    │   └── main.yml
    ├── molecule
    │   └── default
    │       ├── INSTALL.rst
    │       ├── converge.yml
    │       ├── molecule.yml
    │       └── verify.yml
    ├── tasks
    │   └── main.yml
    ├── templates
    ├── tests
    │   ├── inventory
    │   └── test.yml
    └── vars
        └── main.yml

You can write some tests becuase we are fancy and do Test Driven Development `\-_-/`


`molecule create` you spin up the infrastructure defined the molecule.yml file: `molecule/default/molecule.yml`

## TDD Means writing tests first!

In this case we check if oneagent is installed.
`../molecule/default/tests/test_default.yml`

To run tests use:
`molecule test`

Test should fail.

Now write enough code that the tests pass. And thats it. Your role is complete.
