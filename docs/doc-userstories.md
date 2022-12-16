# Documento Lista de User Stories

## Descrição

Este documento descreve os User Stories criados a partir da Lista de Requisitos Funcionais no
[Documento de Visão](https://github.com/labens-ufrn/academic-devflow/blob/doc/issue2/docs/doc-visao.md).

## User Story US01 - Manter Usuário

|                              |                                                                                                                                                                                                                       |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**                | Um usuário tem username, password, tipo de usuário. Os usuários são criados automaticamente no cadastro de cada membro, mas o sistema deve permitir que cada usuário possa visualizar seus dados e também alterá-los. |
| **Requisitos envolvidos**    | RF08                                                                                                                                                                                                                  |
| **Estimativa**               | 5 Horas                                                                                                                                                                                                              | 
| **Tempo Gasto (real):**      | ---                                                                                                                                                                                                                  |
| **Prioridades**              | Essencial                                                                                                                                                                                                            |
| **Tamanho Funcional**        | ---                                                                                                                                                                                                                  |
| **Analista**                 | Guilherme                                                                                                                                                                                                            |
| **Desenvolvedor**            | Não Definido                                                                                                                                                                                                          |
| **Revisor**                  | Não Definido                                                                                                                                                                                                          |
| **Testador**                 | Não Definido                                                                                                                                                                                                          |

### US01 - Testes de aceitação (TA)

| **Código**  | **Descrição** |
|-------------|---------------|
| **TA01.01** | O usuário informa, na tela Registrar, todos os dados para registrar-se corretamente, ao clicar em Salvar ele é notificado com uma mensagem de sucesso. Mensagem: Cadastro realizado com sucesso, aguardando ativação do administrado |
| **TA01.02** | O usuário informa, na tela Registrar, os dados para registrar-se incorretamente, ao clicar em Salvar ele é notificado com uma mensagem de erro. Mensagem: Cadastro não realizado, o campo “xxxx” não foi informado corretamente. |
| **TA01.03** | O usuário informa, na tela Login, os dados para logar corretamente, ao clicar em Entrar ele é notificado com uma mensagem de erro. Mensagem: Usuário não ativado, aguardando ativação do administrador |
| **TA01.04** | O usuário informa, na tela Login, os dados para logar corretamente, ao clicar em Entrar ele é encaminhado para a tela principal do sistema. É exibida a Mensagem: Login realizado com sucesso. |
| **TA01.05** | No seu perfil, ao usuário clicar alterar, deverá ser capaz de alterar a informação desejada |
| **TA01.06** | No seu perfil, os campos que estão sendo alterados deverão ser atualizados corretamente, ao clicar em Salvar ele é notificado com uma mensagem de sucesso. Mensagem: Alteração realizada com sucesso. |
| **TA01.07** | O usuário informa, durante a alteração do perfil, os dados para registrar-se incorretamente, ao clicar em Salvar ele é notificado com uma mensagem de erro. Mensagem: Atualização não realizada, o campo “xxxx” não foi informado. |

## User Story US02 - Acessar Sistema

|                              |                                                                                                                                                                                                                       |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**                | Quando o usuário estiver adicionado suas credenciais, o sistema deverá permitir a liberação dos módulos de acesso, de acordo com a prioridade do usuário, isso irá liberar o acesso as funcionalidades dos componentes já implementados. |
| **Requisitos envolvidos**    | RF03, RF04, RF09, RF10                                                                                                                                                                                                |
| **Estimativa**               | 10 Horas                                                                                                                                                                                                              |
| **Tempo Gasto (real):**      | ---                                                                                                                                                                                                                  |
| **Prioridades**              | Essencial                                                                                                                                                                                                            |
| **Tamanho Funcional**        | ---                                                                                                                                                                                                                  |
| **Analista**                 | Hilário                                                                                                                                                                                                              |
| **Desenvolvedor**            | Não Definido                                                                                                                                                                                                          |
| **Revisor**                  | Não Definido                                                                                                                                                                                                          |
| **Testador**                 | Não Definido                                                                                                                                                                                                          |

### US02 - Testes de aceitação (TA)

| **Código**  | **Descrição** |
|-------------|---------------|
| **TA02.01** | O usuário informa, na tela Login, os dados para logar corretamente, ao clicar em Entrar ele é encaminhado para a tela principal do sistema. É exibida a Mensagem: Login realizado com sucesso. |
| **TA02.02** | O usuário informa, na tela Login, os dados para logar incorretamente, ao clicar em Entrar ele é notificado com uma mensagem de erro. É exibida a Mensagem: Usuário não ativado, aguardando ativação do administrador. |
| **TA02.03** | No seu perfil, o usuário deverá ser capaz de visualizar todas as informações ao qual ele tem acesso. |
| **TA02.04** | No seu perfil, o usuário poderá listar informações desejadas e exportar os dados para um arquivo em formato de planilha, ao clicar em Exportar ele é notificado com uma mensagem de sucesso. É exibida a Mensagem: Lista "xxxx" exportada com sucesso. |

## User Story US03 - Manter projeto

|     |     |
| --- | --- |
| **Descrição** | O sistema deve permitir o cadastro, visualização, edição e exclusão de projetos. Membros podem apenas visualizar as informações dos projetos aos quais fazem parte. Coordenadores podem criar, visualizar e editar projetos que coordenam. Administradores podem realizar as quatro operações de forma irrestrita. Todas as operações demandam que o usuário esteja logado. |
| **Requisitos envolvidos** | RF01, RF02, RNF01, RNF02, RNF03 |
| **Prioridade** | Importante |
| **Estimativa** | 8h |
| **Tempo gasto (real)** | - |
| **Tamanho funcional** | 7PF (Pontos de função) |
| **Analista** | Adriel Faria dos Santos |
| **Desenvolvedor** | - |
| **Revisor** | - |
| **Testador** | - |

### US03 - Testes de aceitação (TA)

| Código | Descrição |
| ------ | --------- |
| TA03.01 | Um usuário não logado tenta visualizar um projeto cadastrado e não consegue, o sistema exibe a mensagem "Você precisa fazer login para visualizar projetos" |
| TA03.02 | Um usuário _Membro_ logado tenta visualizar um projeto do qual não faz parte e não consegue, o sistema exibe a mensagem "Você não possui permipermissão para visualizar esse projeto" |
| TA03.03 | Um usuário _Membro_ logado tenta visualizar um projeto do qual faz parte e consegue, o sistema exibe os dados referentes ao projeto |
| TA03.04 | Um usuário _Coordenador_ logado tenta visualizar um projeto do qual não faz parte e não consegue, o sistema exibe a mensagem "Você não possui permissão para visualizar esse projeto" |
| TA03.05 | Um usuário _Coordenador_ logado tenta visualizar um projeto do qual faz parte e consegue, o sistema exibe os dados referentes ao projeto |
| TA03.06 | Um usuário _Administrador_ logado tenta visualizar um projeto do qual não faz parte e consegue, o sistema exibe os dados referentes ao projeto |
| TA03.07 | Um usuário _Administrador_ logado tenta visualizar um projeto do qual faz parte e consegue, o sistema exibe os dados referentes ao projeto |
| TA03.08 | Um usuário não logado tenta cadastrar um projeto e não consegue, o sistema exibe a mensagem "Você precisa fazer login para cadastrar projetos" |
| TA03.09 | Um usuário _Membro_ logado tenta cadastrar um projeto e não consegue, o sistema exibe a mensagem "Você não possui permissão para cadastrar projetos" |
| TA03.10 | Um usuário _Coordenador_ logado tenta cadastrar um projeto e é direcionado para um formulário com os campos **Nome**, **Descrição** (opcional), **Situação**, **Data de início**, **Data de término**, **Equipe** e **Fluxo** |
| TA03.11 | Um usuário _Coordenador_ preenche o formulário de cadastro de projetos com todos os campos obrigatórios e o submete, o sistema salva o novo projeto e o redireciona para a página de visualização do projeto, que mostra os dados conforme foram preenchidos |
| TA03.12 | Um usuário _Coordenador_ preenche o formulário de cadastro de projetos com todos os campos obrigatórios e opcionais, e o submete, o sistema salva o novo projeto e o redireciona para a página de visualização, que mostra os dados conforme foram preenchidos |
| TA03.13 | Um usuário _Coordenador_ não preenche todos os campos obrigatórios do formulário de cadastro de projetos e o submete, o sistema exibe a mensagem de erro "Há campos obrigatórios não preenchidos" |
| TA03.14 | Um usuário _Administrador_ preenche o formulário de cadastro de projetos com todos os campos obrigatórios e o submete, o sistema salva o novo projeto e o redireciona para a página de visualização do projeto, que mostra os dados conforme foram preenchidos |
| TA03.15 | Um usuário _Administrador_ preenche o formulário de cadastro de projetos com todos os campos obrigatórios e opcionais, e o submete, o sistema salva o novo projeto e o redireciona para a página de visualização, que mostra os dados conforme foram preenchidos |
| TA03.16 | Um usuário _Administrador_ não preenche todos os campos obrigatórios do formulário de cadastro de projetos e o submete, o sistema exibe a mensagem de erro "Há campos obrigatórios não preenchidos" |
| TA03.17 | Um usuário não logado tenta editar um projeto e não consegue, o sistema exibe a mensagem "Você precisa fazer login para editar projetos" |
| TA03.18 | Um usuário _Membro_ logado tenta editar um projeto e não consegue, o sistema exibe a mensagem "Você não possui permissão para editar projetos" |
| TA03.19 | Um usuário _Coordenador_ logado tenta editar um projeto do qual não faz parte e não consegue, o sistema exibe a mensagem "Você não possui permissão para editar esse projeto" |
| TA03.20 | Um usuário _Coordenador_ logado tenta editar um projeto do qual faz parte e é direcionado para um formulário com os campos **Nome**, **Descrição** (opcional), **Situação**, **Data de início**, **Data de término**, **Equipe** e **Fluxo** preenchidos com os dados salvos no banco |
| TA03.21 | Um usuário _Coordenador_ preenche o formulário de edição de projeto, modificando todos os campos obrigatórios, deixando os campos opcionais em branco, e o submete, o sistema salva o projeto e o redireciona para a página de visualização, que mostra os dados conforme foram preenchidos e a mensagem "Alterações salvas" |
| TA03.22 | Um usuário _Coordenador_ preenche o formulário de edição de projeto, modificando todos os campos obrigatórios e opcionais, e o submete, o sistema salva o projeto e o redireciona para a página de visualização, que mostra os dados conforme foram preenchidos e a mensagem "Alterações salvas" |
| TA03.23 | Um usuário _Coordenador_ preenche o formulário de edição de projeto, deixando campos obrigatórios em branco, e o submete, o sistema exibe a mensagem "Há campos obrigatórios não preenchidos" |
| TA03.24 | Um usuário _Administrador_ logado tenta editar um projeto do qual não faz parte e consegue, o sistema o redireciona para um formulário com os campos **Nome**, **Descrição** (opcional), **Situação**, **Data de início**, **Data de término**, **Equipe** e **Fluxo** preenchidos com os dados salvos no banco |
| TA03.25 | Um usuário _Administrador_ logado tenta editar um projeto do qual faz parte e é direcionado para um formulário com os campos **Nome**, **Descrição** (opcional), **Situação**, **Data de início**, **Data de término**, **Equipe** e **Fluxo** preenchidos com os dados salvos no banco |
| TA03.26 | Um usuário _Administrador_ preenche o formulário de edição de projeto, modificando todos os campos obrigatórios, deixando os campos opcionais em branco, e o submete, o sistema salva o projeto e o redireciona para a página de visualização, que mostra os dados conforme foram preenchidos e a mensagem "Alterações salvas" |
| TA03.27 | Um usuário _Administrador_ preenche o formulário de edição de projeto, modificando todos os campos obrigatórios e opcionais, e o submete, o sistema salva o projeto e o redireciona para a página de visualização, que mostra os dados conforme foram preenchidos e a mensagem "Alterações salvas" |
| TA03.28 | Um usuário _Administrador_ preenche o formulário de edição de projeto, deixando campos obrigatórios em branco, e o submete, o sistema exibe a mensagem "Há campos obrigatórios não preenchidos" |
| TA03.29 | Um usuário não logado tenta excluir um projeto e não consegue, o sistema exibe a mensagem "Você precisa fazer login para excluir projetos" |
| TA03.30 | Um usuário _Membro_ logado tenta excluir um projeto e não consegue, o sistema exibe a mensagem "Você não possui permissão para excluir projetos" |
| TA03.31 | Um usuário _Coordenador_ logado tenta excluir um projeto e não consegue, o sistema exibe a mensagem "Você não possui permissão para excluir projetos" |
| TA03.32 | Um usuário _Administrador_ logado tenta excluir um projeto e o sistema exibe um forulário com botões para confirmar ou cancelar a operação, o usuário confirma a operação, o sistema exclui o registro, o redireciona para a página inicial e exibe a mensagem "Projeto excluido" |
| TA03.33 | Um usuário _Administrador_ logado tenta excluir um projeto e o sistema exibe um forulário com botões para confirmar ou cancelar a operação, o usuário cancela a operação e o sistema mantém o registro |

## User Story US04 - Manter Fluxo de desenvolvimento

|           |           |
| --------- | --------- |
| **Descrição:** | Um fluxo de desenvolvimento tem código, nome, descrição, quantidade de etapas. O sistema deve permitir o cadastro de um novo fluxo de desenvolvimento para cada projeto, assim como a alteração e visualização deste. |
| **Requisitos Envolvidos** | RF03 | Manter Fluxo de desenvolvimento |
| **Prioridade**            | Essencial |
| **Estimativa**            | 8h |
| **Tempo Gasto (real):**   | --- |
| **Tamanho Funcional**     | --- |
| **Analista**              | Hilario |
| **Desenvolvedor**         | Adriel  |
| **Revisor**               | Guilherme |
| **Testador**              | Guilherme  |

### US04 - Testes de Aceitação (TA)

| **Código**  | **Descrição** |
| ----------- | ------------- |
| **TA04.01** | O usuário deseja cadastrar um novo fluxo de desenvolvimento, então o usuário clica no botão inserir fluxo de desenvolvimento. O usuário preenche todos os campos de modo correto e clica em Salvar/Cadastrar, recebendo uma notificação em tela de sucesso, como "Fluxo de desenvolvimento cadastrado com sucesso". |
| **TA04.02** | O usuário deseja cadastrar um novo fluxo de desenvolvimento, então o usuário clica no botão inserir fluxo de desenvolvimento. O usuário preenche algum campo ou todos os campos de modo incorreto e clica em Salvar/Cadastrar, o usuário é notificado com uma mensagem de erro. Mensagem: Cadastro não realizado, o campo “xxxx” não foi informado corretamente. |
| **TA04.03** | O usuário deseja alterar o fluxo de desenvolvimento, então o usuário clica no botão editar fluxo de desenvolvimento. O usuário altera os campos que deseja de modo correto e clica em Editar/Salvar, recebendo uma notificação em tela de sucesso, como "Fluxo de desenvolvimento alterado com sucesso". |                                                     
| **TA04.04** | O usuário deseja alterar o fluxo de desenvolvimento, então o usuário clica no botão editar fluxo de desenvolvimento. O usuário altera algum campo ou todos os campos de modo incorreto e clica em Editar/Salvar, o usuário é notificado com uma mensagem de erro. Mensagem: A operação falhou, o campo “xxxx” não foi informado corretamente. | 
| **TA04.05** | O usuário deseja excluir o fluxo de desenvolvimento, o usuário clica no botão excluir, caso o fluxo de desenvolvimento já possua etapas cadastradas, o sistema deve informar ao usuário e perguntar se realmente deseja excluir o fluxo de desenvolvimento, caso o usuário confirme, o sistema envia o fluxo para a lixeria e notifica ao usuário com uma mensagem de sucesso. Mensagem: "Fluxo de desenvolvimento excluído com sucesso".   Caso o usuário não confirme, ele deve ser notificado com uma mensagem informando que nenhuma mudança ocorreu. |          

## User Story US05 - Manter etapa

|     |     |
| --- | --- |
| **Descrição** | O sistema deve permitir o cadastro, visualização, edição e exclusão de etapas de fluxos. Membros podem apenas visualizar as informações dos projetos aos quais fazem parte. Coordenadores podem criar, visualizar e editar etapas dos fluxos criados por ele, nos casos de fluxos criados por outros usuários, apenas a visualização é possível, a exclusão é permitida apenas quando o coordenador faz parte do projeto e a etapa não foi iniciada ainda. Administradores podem realizar as quatro operações de forma irrestrita, exceto ao tentar excluir uma etapa que já iniciou. Todas as operações demandam que o usuário esteja logado. |
| **Requisitos envolvidos** | RF01, RF03, RF04, RNF01, RNF02, RNF03 |
| **Prioridade** | Importante |
| **Estimativa** | 10h |
| **Tempo gasto (real)** | - |
| **Tamanho funcional** | 7PF (Pontos de função) |
| **Analista** | Adriel Faria dos Santos |
| **Desenvolvedor** | - |
| **Revisor** | - |
| **Testador** | - |

### US05 - Testes de aceitação (TA)

| Código  | Descrição |
| ------- | --------- |
| TA05.01 | Um usuário deseja visualizar uma etapa de um fluxo de projeto. O usuário não está logado. O sistema o redireciona para a tela de login. |
| TA05.02 | Um usuário deseja editar uma etapa de um fluxo de projeto. O usuário não está logado. O sistema o redireciona para a tela de login. |
| TA05.03 | Um usuário deseja excluir uma etapa de um fluxo de projeto. O usuário não está logado. O sistema o redireciona para a tela de login. |
| TA05.04 | Um usuário deseja adicionar uma etapa a um fluxo de projeto. O usuário não está logado. O sistema o redireciona para a tela de login. |
| TA05.05 | Um usuário aluno deseja visualizar uma etapa de um fluxo de projeto. O usuário não faz parte daquele projeto. O sistema impede a visualização. |
| TA05.06 | Um usuário aluno deseja visualizar uma etapa de um fluxo de projeto. O usuário faz parte daquele projeto. O sistema permite a visualização, o redirecionando para a tela de visualização de etapa. |
| TA05.07 | Um usuário aluno deseja editar uma etapa de um fluxo de projeto. O sistema impede a edição. |
| TA05.08 | Um usuário aluno deseja excluir uma etapa de um fluxo de projeto. O sistema impede a exclusão. |
| TA05.09 | Um usuário aluno deseja adicionar uma etapa a um fluxo de projeto. O sistema impede a criação. |
| TA05.10 | Um usuário coordenador deseja visualizar uma etapa de um fluxo de projeto. O sistema permite a visualização, o redirecionando para a tela de visualização de etapa. |
| TA05.11 | Um usuário coordenador deseja editar uma etapa de um fluxo de projeto. O usuário não faz parte do projeto. O sistema impede a edição. |
| TA05.12 | Um usuário coordenador deseja editar uma etapa de um fluxo de projeto. O usuário faz parte do projeto. O sistema permite a edição, mostrando um formulário já preenchido com os campos nome, descrição (opcional), data de início, data de finalização, usar gameficação, e posicao da etapa no fluxo. O usuário altera alguns campos, mas todos os campos obrigatórios estão preenchidos. O usuário submete o formulário. O sistema altera a etapa. |
| TA05.13 | Um usuário coordenador deseja excluir uma etapa de um fluxo de projeto. O usuário faz parte do projeto e ainda não iniciou. O sistema permite a exclusão, mostrando uma caixa de confirmação. O usuário confirma a exclusão. O sistema exclui a etapa. |
| TA05.14 | Um usuário coordenador deseja excluir uma etapa de um fluxo de projeto. O usuário faz parte do projeto mas ela já iniciou. O sistema impede a exclusão. |
| TA05.15 | Um usuário coordenador deseja excluir uma etapa de um fluxo de projeto. O usuário faz parte do projeto. O sistema impede a exclusão. |
| TA05.16 | Um usuário coordenador deseja adicionar uma etapa a um fluxo de projeto. O usuário não faz parte do projeto. O sistema impede a criação. |
| TA05.17 | Um usuário coordenador deseja adicionar uma etapa a um fluxo de projeto. O usuário faz parte do projeto. O sistema permite a criação, mostrando um formulário com os campos nome, descrição (opcional), data de início, data de finalização, usar gameficação, e posicao da etapa no fluxo. O usuário preenche todos os campos obrigatórios e o campo data de finalização tem um valor superior ou igual a dataatual. O usuário submete o formulário. O sistema cria a etapa. |
| TA05.18 | Um usuário coordenador deseja adicionar uma etapa a um fluxo de projeto. O usuário faz parte do projeto. O sistema permite a criação, mostrando um formulário com os campos nome, descrição (opcional), data de início, data de finalização, usar gameficação, e posicao da etapa no fluxo. O usuário preenche todos os campos obrigatórios e o campo data de finalização tem um valor inferior a data atual. O sistema não permite a submissão do formulário, exibindo a mensagem de validação "A etapa não pode finalizar em uma data anteior a hoje". |
| TA05.19 | Um usuário administrador deseja visualizar uma etapa de um fluxo de projeto. O sistema redireciona para a tela de visualização de etapa. |
| TA05.20 | Um usuário administrador deseja editar uma etapa de um fluxo de projeto. O sistema permite a edição, mostrando um formulário já preenchido com os campos nome, descrição (opcional), data de início, data de finalização, usar gameficação, e posicao da etapa no fluxo. O usuário altera alguns campos, mas todos os campos obrigatórios estão preenchidos. O usuário submete o formulário. O sistema altera a etapa. |
| TA05.21 | Um usuário administrador deseja excluir uma etapa de um fluxo de projeto. O etapa ainda não iniciou. O sistema permite a exclusão, mostrando uma caixa de confirmação. O usuário confirma a exclusão. O sistema exclui a etapa. |
| TA05.22 | Um usuário administrador deseja excluir uma etapa de um fluxo de projeto, mas ela já iniciou. O sistema impede a exclusão. |
| TA05.23 | Um usuário administrador deseja adicionar uma etapa a um fluxo de projeto. O sistema permite a criação, mostrando um formulário com os campos nome, descrição (opcional), data de início, data de finalização, usar gameficação, e posicao da etapa no fluxo. O usuário preenche todos os campos obrigatórios. O usuário submete o formulário. O sistema cria a etapa. |

## User Story US06 - Manter Iteração

|     |     |
| --- | --- |
| **Descrição** | O sistema deve permitir o cadastro, visualização, edição e exclusão das iterações. Uma iteração tem código, data de início, data de término e uma descrição. As informações referentes a iteração pode ser manipuladas pelos coordenadores e  também pelos membros responsáveis pelo desenvolvimento do projeto.Todas as operações demandam que o usuário esteja logado. |
| **Requisitos envolvidos** | RF01, RF02, RF11, RNF1, RNF2, RNF3 | 
| **Prioridade** | Importante |
| **Estimativa** | 10h |
| **Tempo gasto (real)** | - |
| **Tamanho funcional** | - |
| **Analista** | Adriel |
| **Desenvolvedor** | - |
| **Revisor** | - |
| **Testador** | - |

### US05 - Testes de aceitação (TA)

| Código  | Descrição |
| ------- | --------- |
| TA06.01 | Um usuário deseja visualizar uma das iterações do projeto. O usuário não está logado. O sistema o redireciona para a tela de login. |
| TA06.02 | Um usuário deseja editar uma das iterações do projeto. O usuário não está logado. O sistema o redireciona para a tela de login. |
| TA06.03 | Um usuário deseja excluir uma das iterações do projeto. O usuário não está logado. O sistema o redireciona para a tela de login. |
| TA06.04 | Um usuário deseja adicionar uma nova iteração ao projeto. O usuário não está logado. O sistema o redireciona para a tela de login. |
| TA06.05 | Um usuário deseja cadastrar uma nova iteração. O usuário está logado. O usuário deve então clicar na opção "Iteração" disponível no menu. Após isso, o usuário deve ser direcionado para a tela de iterações existentes do projeto. O usuário clica no botão "Nova Iteração". O sistema direciona o usuário para uma tela contendo um formulário. O usuário preenche corretamente as informações do formulário de registro de uma nova iteração e clica no botão salvar. O sistema deve informar ao usuário que a operação foi concluída com sucesso e direcioná-lo para a tela de iterações. |
| TA06.06 | Um usuário deseja cadastrar uma nova iteração. O usuário está logado. O usuário deve então clicar na opção "Iteração" disponível no menu. Após isso, o usuário deve ser direcionado para a tela de iterações existentes do projeto. O usuário clica no botão "Nova Iteração". O sistema direciona o usuário para uma tela contendo um formulário. O usuário preenche incorretamente as informações do formulário e clica no botão "Salvar". O sistema deve informar ao usuário que o formulário foi preenchido incorretamente, além de informar quais campos foram preenchidos incorretamente. |
| TA06.07  | Um usuário deseja visualizar um iteração. O usuário está logado. O usuário deve então clicar na opção "Iteração" disponível no menu. Após isso, o usuário deve ser direcionado para a tela de iterações existentes do projeto. O usuário identifica a iteração que deseja visualizar e a seleciona. O sistema deve exibir uma interface contendo o nome da iteração, a data de início e fim, e a sua descrição. Além disso, deve ser mostrado quantas atividades estão vinculados a esta iteração, assim como a quantidade de artefatos. |
| TA06.08 | Um usuário deseja editar as informações de uma iteração. O usuário está logado. O usuário deve então clicar na opção "Iteração" disponível no menu. Após isso, o usuário deve ser direcionado para a tela de iterações existentes do projeto. O usuário identifica a iteração que deseja editar e a seleciona. O sistema deve exibir uma interface contendo as informações da iteração e um botão de editar. Ao clicar no botão editar, o sistema direciona o usuário para uma tela contendo um formulário preenchido com as informações atuais da iteração. O usuário preenche corretamente as informações que deseja alterar e clica no botão salvar. O sistema deve informar ao usuário que a operação foi concluída com sucesso e direcioná-lo para a tela de iterações. |
| TA06.09 | Um usuário deseja editar as informações de uma iteração. O usuário está logado. O usuário deve então clicar na opção "Iteração" disponível no menu. Após isso, o usuário deve ser direcionado para a tela de iterações existentes do projeto. O usuário identifica a iteração que deseja editar e a seleciona. O sistema deve exibir uma interface contendo as informações da iteração e um botão de editar. Ao clicar no botão editar, o sistema direciona o usuário para uma tela contendo um formulário preenchido com as informações atuais da iteração. O usuário preenche incorretamente as informações que deseja alterar e clica no botão salvar. O sistema deve informar ao usuário que o formulário foi preenchido incorretamente, além de informar quais campos foram preenchidos incorretamente. |
| TA06.10 | Um usuário deseja excluir uma iteração que já se encontra em andamento. O usuário está logado. O usuário deve então clicar na opção "Iteração" disponível no menu. Após isso, o usuário deve ser direcionado para a tela de iterações existentes do projeto. O usuário identifica a iteração que deseja excluir e a seleciona. O sistema deve exibir uma interface contendo as informações da iteração e um botão de excluir. O usuário clica no botão "excluir". O sistema deve informar que a iteração encontra-se em andamento e informar que não é possível a exclusão da iteração. |
| TA06.11 | Um usuário deseja excluir uma iteração que ainda não começou e ainda não possui nem atividades e nem artefatos. O usuário está logado. O usuário deve então clicar na opção "Iteração" disponível no menu. Após isso, o usuário deve ser direcionado para a tela de iterações existentes do projeto. O usuário identifica a iteração que deseja excluir e a seleciona. O sistema deve exibir uma interface contendo as informações da iteração e um botão de excluir. O usuário clica no botão "excluir". O sistema deve informar ao usuário que a operação foi concluída com sucesso e direcioná-lo para a tela de iterações. |

### US07 - Manter Artefato

|            |            |
|------------|------------|
|**descrição**            | O sistema deve permitir que seja realizado o cadastro, leitura, update e delete de artefatos. Além disso, um artefato está associado a um projeto, etapa e iteraçao, possibilitando realizar o controle de qual projeto, etapa e iteração tal artefato pertence. Os artefatos ajudarão a dar suporte ao andamento do projeto, auxiliando também no planejamento. |
|**Requisitos envolvidos**| RF09, RF18 ,RF19 |
|**Prioridade**           | importante |
|**Estimativa**           | 10h |
|**Tempo gasto (real)**   | - |
|**Tamanho Funcional**    | 7 |
|**Analista**             | Guilherme Angelo de Medeiros |
| **Revisor**             | - |
| **Testador**            | - |

### US07 - Testes de Aceitação (TA)

| Código | Descrição |
|-----|-----|
| TA07.01 | O usuário informa na tela as informações necessárias ao cadastro do artefato, ao clicar no botão salvar os dados deve ser exibida uma mensagem de confirmação.|
| TA07.02 | Ao clicar em "listar artefato", Todos os artefatos que ainda não foram entregues devem ser exibidos, assim também como os recém cadastrados. |
| TA07.03 | Caso o usuário preencha alguns dos campos incorretamente durante o cadastro, deve ser exibida uma mensagem alertando qual campo foi preenchido incorretamente, além disso, os dados da tentativa fracassada não podem ser armazenados. |
| TA07.04 | Na listagem de Artefato o responsável pelo projeto poderá alterar o artefato clicando em "Alterar", posteriormente ele deverá preencher qual ou quais campos ele deseja alterar. Quando realizada a alteração uma mesagem de sucesso deve ser exibida, confimando que a alteração foi realizada com sucesso. |
| TA07.05 | O responsável pelo projeto durante a alteração do artefato preenche informações inválidas, ao clicar em "Salvar" deve ser exibida um mensagem de erro, alertando o usuário qual(is) campo(s) foi preenchido incorretamente. |
| TA07.06 | O Artefato no momento em que responsável pelo projeto ao clicar em "deletar" deve ser excluido, e uma mesagem de sucesso deve ser exibida. |

### US08 - Manter Coordenador

|            |            |
|------------|------------|
|**descrição**            | O sistema deve permitir que seja realizado o insert, read, update e delete de coordenadores. Além disso, um coordenador é um usuário do sistema e está associado à nenhum ou vários projetos,contudo o projeto será coordenado apenas por um coodenador, também está associado a uma equipe , possibilitando realizar o controle e gerenciamento de seus membros, sendo assim, o coordenado também é membro de uma equipe |
|**Requisitos envolvidos**| RF02, RF04 ,RF06, RF07 |
|**Prioridade**           | importante |
|**Estimativa**           | 10h |
|**Tempo gasto (real)**   | - |
|**Tamanho Funcional**    | 10 |
|**Analista**             | Hilário Dantas |
| **Revisor**             | Guilherme Ângelo |
| **Testador**            | Adriel Faria |

### US08 - Teste de Aceitação(TA)

| Código | Descrição |
|-----|-----|
| TA08.01 | O usuário informa na tela as informações necessárias ao cadastro do coordenado, ao clicar no botão salvar os dados deve ser exibida uma mensagem de confirmação de cadastro.|
| TA08.02 | Ao clicar em "listar coordenadores", todos os coordenadores devem ser exibidos, com sua respectiva(as) equipes e projeto(s)|
| TA08.03 | Caso o usuário preencha alguns dos campos incorretamente durante o cadastro, deve ser exibida uma mensagem alertando qual campo foi preenchido incorretamente, além disso, os dados da tentativa fracassada não podem ser armazenados. |
| TA08.04 | Na listagem de coordenadores o responsável pelo projeto poderá alterar as informações do coordenador clicando em "Alterar", posteriormente ele deverá preencher qual ou quais campos ele deseja alterar. Quando realizada a alteração uma mesagem de sucesso deve ser exibida, confimando que a alteração foi realizada com sucesso. |
| TA08.05 | O responsável pelo projeto durante a alteração dos dados do coordenador preenche informações inválidas, ao clicar em "Salvar" deve ser exibida um mensagem de erro, alertando o usuário qual(is) campo(s) foi preenchido incorretamente. |
| TA08.06 | No momento em que o responsável clicar em "deletar" o coornador deve ser excluido, e uma mesagem de sucesso deve ser exibida. Além disso, os projetos, equipes que ele esteja associado deverão apresentar o valor padrão |
| TA08.07 | Realizado o cadastro, o coordenador poderá ou não estar associado a uma equipe ou projeto. Com isso deverão ser testadas as duas possibilidades e ambas devem receber confirmações de sucesso. |

### US09 - Manter Equipe

|            |            |
|------------|------------|
|**descrição**            | O sistema deve ser capaz de realizar o cadastro de equipe, inserindo também seus respectivos membros, projeto e coodenador. Além disso, deve ser capaz de realizar updates em seus respectivos atributos, leitura e delete. Uma equipe é composta por membros, é coordenada por um usuário coordenador e está associada a um projeto.|
|**Requisitos envolvidos**| RF02, RF05 ,RF06, RF07|
|**Prioridade**           | importante |
|**Estimativa**           | 10h |
|**Tempo gasto (real)**   | - |
|**Tamanho Funcional**    | 10 |
|**Analista**             | Guilherme Angelo de Medeiros |
| **Revisor**             | Hilário Dantas |
| **Testador**            | Adriel Faria |

### US09 - Teste de Aceitação(TA)

| Código | Descrição |
|-----|-----|
| TA09.01 | O informa informa na tela as informações necessárias ao cadastro da equipe, ao clicar no botão salvar os dados deve ser exibida uma mensagem de confirmação.|
| TA09.02 | Ao clicar em "listar equpes", Todos as equipes que existam devem ser exibidas.|
| TA09.03 | Caso o usuário preencha alguns dos campos incorretamente durante o cadastro, deve ser exibida uma mensagem alertando qual campo foi preenchido incorretamente, além disso, os dados da tentativa fracassada não podem ser armazenados. |
| TA09.04 | Na listagem de equipes o responsável pelo projeto poderá alterar a equipe clicando em "Alterar", posteriormente ele deverá preencher qual ou quais campos ele deseja alterar. Quando realizada a alteração, uma mesagem de sucesso deve ser exibida, confimando que a alteração foi realizada com sucesso. |
| TA09.05 | O responsável pelo projeto durante a alteração da equipe preenche informações inválidas, ao clicar em "Salvar" deve ser exibida um mensagem de erro, alertando o usuário qual(is) campo(s) foi preenchido incorretamente. |
| TA09.06 | A equipe no momento em que responsável ao clicar em "deletar" deve ser excluido a equipe, os membros e o projeto devem continuar existindo. Contudo, não devem fazer parte da equipe excluida e uma mesagem de sucesso deve ser exibida ao fim da exclusão. |

### US10 - Manter Membro

|            |            |
|------------|------------|
|**descrição**            | O sistema deve permitir que seja realizado o cadastro, leitura, update e delete de membros. Além disso, o membro é um usuário que pode coodenar ou ser coordenado e ele pode percetencer a nenhuma ou várias equipes. |
|**Requisitos envolvidos**| RF05, RF06 ,RF07, RF08 |
|**Prioridade**           | importante |
|**Estimativa**           | 10h |
|**Tempo gasto (real)**   | - |
|**Tamanho Funcional**    | 10 |
|**Analista**             | Adriel Faria |
| **Revisor**             | Hilário Dantas |
| **Testador**            | Guilherme Ângelo |

### US10 - Teste de Aceitação(TA)

| Código | Descrição |
|-----|-----|
| TA10.01 | O usuário informa na tela as informações necessárias ao cadastro do membro, ao clicar no botão salvar os dados deve ser exibida uma mensagem de confirmação.|
| TA10.02 | Ao clicar em "listar membros", Todos os membros devem ser exibidos juntamente com sua respectiva equipe. |
| TA10.03 | Caso o usuário preencha alguns dos campos incorretamente durante o cadastro, deve ser exibida uma mensagem alertando qual campo foi preenchido incorretamente, além disso, os dados da tentativa fracassada não podem ser armazenados. |
| TA10.04 | Na listagem de membros o responsável pelo projeto poderá alterar os dados do membro clicando em "Alterar", posteriormente, ele deverá preencher qual ou quais campos ele deseja alterar. Quando realizada a alteração uma mesagem de sucesso deve ser exibida, confimando que a alteração foi realizada com sucesso. |
| TA10.05 | O responsável pelo projeto durante a alteração do artefato preenche informações inválidas, ao clicar em "Salvar" deve ser exibida um mensagem de erro, alertando o usuário qual(is) campo(s) foi preenchido incorretamente. |
| T10.06 | O membro no momento em que responsável pelo projeto ao clicar em "deletar" deve ser excluido, e uma mesagem de sucesso deve ser exibida. |

### US11 - Manter Atividade

|     |     |
| --- | --- |
| **Descrição** | O sistema deve permitir o cadastro, visualização, edição e exclusão das atividades. Uma atividade tem código, nome, descrição, situação, data de início, data de conclusão, projeto, responsável. As informações referentes a atividade podem ser manipuladas pelos coordenadores e visualizadas pelos membros responsáveis pelo desenvolvimento do projeto. Todas as operações demandam que o usuário esteja logado. |
| **Requisitos envolvidos** | RF01, RF02, RF10, RNF1, RNF2, RNF3 | 
| **Prioridade** | Importante |
| **Estimativa** | 10h |
| **Tempo gasto (real)** | - |
| **Tamanho funcional** | - |
| **Analista** | Adriel Faria dos Santos |
| **Desenvolvedor** | - |
| **Revisor** | - |
| **Testador** | - |

### US11 - Testes de Aceitação (TA)

| Código | Descrição |
|-----|-----|
| TA11.01 | O usuário acessa um projeto que coordena e clica no botão adicionar atividade. O sistema o redireciona para a tela de cadastro de atividade, onde há um formulário com os campos nome, descrição, data de início, data de conclusão e responsável, o usuário preenche os campos obrigatórios e submete o formulário. O sistema salva a nova atividade e o redireciona para a tela de projeto, na qual exibe a mensagem "Atividade cadastrada". |
| TA11.02 | O usuário acessa um projeto que coordena e clica no botão adicionar atividade. O sistema o redireciona para a tela de cadastro de atividade, onde há um formulário com os campos nome, descrição, data de início, data de conclusão e responsável, o usuário não preenche todos os campos obrigatórios e tenta submeter o formulário. O sistema não permite a submissão e não salva a nova atividade, exibindo uma mensagem referente ao erro de validação do formulário. |
| TA11.03 | O usuário acessa uma atividade de um projeto que coordena e clica no botão editar atividade. O sistema o redireciona para a tela de edição de atividade, onde há um formulário com os campos nome, descrição, data de início, data de conclusão e responsável, já preenchidos com os valores salvos atualmente. O usuário preenche os campos obrigatórios e submete o formulário. O sistema salva as alterações e o redireciona para a tela de projeto, na qual exibe a mensagem "Atividade atualizada". |
| TA11.04 | O usuário acessa uma atividade de um projeto que coordena e clica no botão editar atividade. O sistema o redireciona para a tela de edição de atividade, onde há um formulário com os campos nome, descrição, data de início, data de conclusão e responsável, já preenchidos com os valores salvos atualmente. O usuário não preenche todos os campos obrigatórios e tenta submeter o formulário. O sistema não permite a submissão e não salva as alterações, exibindo uma mensagem referente ao erro de validação do formulário. |
| TA11.05 | O usuário acessa uma atividade de um projeto que coordena e clica no botão excluir atividade. O sistema o redireciona para a tela de confirmação de exclusão, onde é exibida a mensagem "Apagar a atividade?" e os botões "Apagar" e "Cancelar". O usuário aperta o botão "Apagar". O sistema exclui a atividade e o redireciona para a tela de projeto, na qual exibe a mensagem "Atividade apagada". |
| TA11.06 | O usuário acessa uma atividade de um projeto que coordena e clica no botão excluir atividade. O sistema o redireciona para a tela de confirmação de exclusão, onde é exibida a mensagem "Apagar a atividade?" e os botões "Apagar" e "Cancelar". O usuário aperta o botão "Cancelar". O sistema não apaga a atividade e redireciona o usuário a página de projeto. |
| TA11.07 | O usuário acessa um projeto que coordena. Entre os detalhes do projeto estão as atividades referentes aquele projeto, com cada uma exibindo nome e situação. O usuário clica no nome de uma das atividades. O sistema o redireciona para a tela de visualização de atividade, na qual as informações nome, descrição, situação, data de início, data de conclusão e responsável aparecem. |
| TA11.08 | O usuário acessa um projeto do qual é membro. Entre os detalhes do projeto estão as atividades referentes aquele projeto em que ele é responsável, com cada uma exibindo nome e situação. O usuário clica no nome de uma das atividades. O sistema o redireciona para a tela de visualização de atividade, na qual as informações nome, descrição, situação, data de início, data de conclusão e responsável aparecem. |


### US12 - Manter plano de iteração

|     |     |
| --- | --- |
| **Descrição** | O sistema deve permitir o cadastro do plano de iteração, assim como a visualização, alteração e exclusão. Um plano de iterações tem dono, lista de projetos e uma lista de iterações. As informações referentes ao plano de iteração podem ser manipuladas pelos coordenadores. Todas as operações demandam que o usuário esteja logado. |
| **Requisitos envolvidos** | RF01, RF11, RNF1, RNF2, RNF3 | 
| **Prioridade** | Desejável |
| **Estimativa** | 10h |
| **Tempo gasto (real)** | - |
| **Tamanho funcional** | - |
| **Analista** | Adriel Faria dos Santos |
| **Desenvolvedor** | - |
| **Revisor** | - |
| **Testador** | - |

### US12 - Testes de Aceitação (TA)

| Código | Descrição |
|-----|-----|
| TA12.01 | O usuário acessa a página de planos de iteração e clica no botão adicionar novo plano de iteração. O sistema o redireciona para a tela de cadastro de plano de iteração, onde há um formulário com os campos projeto e iterações, no qual ele pode selecionar um ou mais projetos que coordena e várias iterações que ele já tenha salvo ou adicionar uma nova a partir do botão "nova iteração". O usuário seleciona os projetos as iterações que ele deseja incluir naquele plano e submete o formulário. O sistema salva o novo plano de iterações e o redireciona para a tela de planos iteração, na qual exibe a mensagem "Plano de iteração cadastrado". |
| TA12.02 | O usuário acessa a página de planos de iteração e seleciona um de seus planos de iteração. O sistema o redireciona para a tela de visualização de plano de iteração, onde exibe os projetos a que aquele plano está atrelado e detalhes das iterações que o compõem. |
| TA12.03 | O usuário acessa a página de visualização de um de seus planos de iteração e seleciona o botão editar. O sistema o redireciona para a tela de edição de plano de iteração, onde há um formulário com os campos projeto e iterações, no qual ele pode selecionar um ou mais projetos que coordena e várias iterações que ele já tenha salvo ou adicionar uma nova a partir do botão "nova iteração". Os projetos e iterações já presentes naquele plano vêm selecionados por padrão. O usuário modifica os projetos e as iterações que utilizam aquele plano e submete o formulário. O sistema salva as modificações e o redireciona para a tela de visualização de planos de iteração, na qual a mensagem "Plano de iteração atualizado" é exibida. |
| TA12.04 | O usuário acessa a página de visualização de um de seus planos de iteração e seleciona o botão excluir. O sistema verifica se aquele plano pertence a algum projeto e determina que não. O sistema redireciona o usuário para a tela de confirmação de exclusão, onde é exibida a mensagem "Apagar o plano de iterações?" e os botões "Apagar" e "Cancelar". O usuário aperta o botão "Apagar". O sistema apaga o plano de iterações e redireciona o usuário a página de planos de iteração, na qual exibe a mensagem "Plano de iterações apagado". |
| TA12.05 | O usuário acessa a página de visualização de um de seus planos de iteração e seleciona o botão excluir. O sistema verifica se aquele plano pertence a algum projeto e determina que não. O sistema redireciona o usuário para a tela de confirmação de exclusão, onde é exibida a mensagem "Apagar o plano de iterações?" e os botões "Apagar" e "Cancelar". O usuário aperta o botão "Cancelar". O sistema não apaga o plano de iterações e redireciona o usuário a página de planos de iteração. |
| TA12.06 | O usuário acessa a página de visualização de um de seus planos de iteração e seleciona o botão excluir. O sistema verifica se aquele plano pertence a algum projeto e determina que sim. O sistema redireciona o usuário para a página de planos de iteração, na qual a mensagem "Remova os projetos do plano de iteração antes de excluí-lo" é exibida. |

### US13 - Manter plano de release

|     |     |
| --- | --- |
| **Descrição** | O sistema deve permitir o cadastro do plano de release, assim como a visualização, alteração e exclusão. Um plano de releases tem dono, lista de projetos e uma lista de releases. As informações referentes ao plano de iteração podem ser manipuladas pelos coordenadores. Todas as operações demandam que o usuário esteja logado. |
| **Requisitos envolvidos** | RF01, RF11, RNF1, RNF2, RNF3 | 
| **Prioridade** | Desejável |
| **Estimativa** | 10h |
| **Tempo gasto (real)** | - |
| **Tamanho funcional** | - |
| **Analista** | Adriel Faria dos Santos |
| **Desenvolvedor** | - |
| **Revisor** | - |
| **Testador** | - |

### US13 - Testes de Aceitação (TA)

| Código | Descrição |
|-----|-----|
| TA13.01 | O usuário acessa a página de planos de release e clica no botão adicionar novo plano de release. O sistema o redireciona para a tela de cadastro de plano de release, onde há um formulário com os campos projeto e releases, no qual ele pode selecionar um ou mais projetos que coordena e várias releases que ele já tenha salvo ou adicionar uma nova a partir do botão "nova release". O usuário seleciona os projetos e as releases que ele deseja incluir naquele plano e submete o formulário. O sistema salva o novo plano de releases e o redireciona para a tela de planos de release, na qual exibe a mensagem "Plano de release cadastrado". |
| TA13.02 | O usuário acessa a página de planos de release e seleciona um de seus planos de release. O sistema o redireciona para a tela de visualização de plano de release, onde exibe os projetos a que aquele plano está atrelado e detalhes das releases que o compõem. |
| TA13.03 | O usuário acessa a página de visualização de um de seus planos de release e seleciona o botão editar. O sistema o redireciona para a tela de edição de plano de release, onde há um formulário com os campos projeto e releases, no qual ele pode selecionar um ou mais projetos que coordena e várias releases que ele já tenha salvo ou adicionar uma nova a partir do botão "nova release". Os projetos e releases já presentes naquele plano vêm selecionados por padrão. O usuário modifica os projetos e as releases que utilizam aquele plano e submete o formulário. O sistema salva as modificações e o redireciona para a tela de visualização de planos de release, na qual a mensagem "Plano de release atualizado" é exibida. |
| TA13.04 | O usuário acessa a página de visualização de um de seus planos de release e seleciona o botão excluir. O sistema verifica se aquele plano pertence a algum projeto e determina que não. O sistema redireciona o usuário para a tela de confirmação de exclusão, onde é exibida a mensagem "Apagar o plano de release?" e os botões "Apagar" e "Cancelar". O usuário aperta o botão "Apagar". O sistema apaga o plano de release e redireciona o usuário a página de planos de release, na qual exibe a mensagem "Plano de release apagado". |
| TA13.05 | O usuário acessa a página de visualização de um de seus planos de release e seleciona o botão excluir. O sistema verifica se aquele plano pertence a algum projeto e determina que não. O sistema redireciona o usuário para a tela de confirmação de exclusão, onde é exibida a mensagem "Apagar o plano de release?" e os botões "Apagar" e "Cancelar". O usuário aperta o botão "Cancelar". O sistema não apaga o plano de release e redireciona o usuário a página de planos de release. |
| TA13.06 | O usuário acessa a página de visualização de um de seus planos de release e seleciona o botão excluir. O sistema verifica se aquele plano pertence a algum projeto e determina que sim. O sistema redireciona o usuário para a página de planos de release, na qual a mensagem "Remova os projetos do plano de release antes de excluí-lo" é exibida. |

### US14 - Emitir relatório

|     |     |
| --- | --- |
| **Descrição** | O sistema deve ser capaz de emitir relatórios com informações acerca de equipes, membros e projetos. |
| **Requisitos envolvidos** | RF01, RF6, RF7, RF15, RNF1, RNF2, RNF5 | 
| **Prioridade** | Desejável |
| **Estimativa** | 10h |
| **Tempo gasto (real)** | - |
| **Tamanho funcional** | - |
| **Analista** | Hilário Petronio de Medeiros Dantas |
| **Desenvolvedor** | - |
| **Revisor** | - |
| **Testador** | - |

### US14 - Testes de Aceitação (TA)

| Código | Descrição |
|-----|-----|
| TA14.01 | O usuário acessa a página de relatórios e clica no botão emitir relatório de equipe, um relatório com informações da equipe, projeto, artefatos, atividades e pontuações deve ser mostrado na tela.| 
| TA14.02 | O usuário acessa a página de relatórios e clica no botão emitir relatório de membro, um relatório com informações da equipe, projeto, artefatos, atividades e pontuações deve ser mostrado na tela.| 
| TA14.03 | O usuário acessa a página de relatórios e clica no botão emitir relatório de projetos ativos, um relatório com uma lista de todos os projetos ativos deve ser mostrado na tela.| 
 
