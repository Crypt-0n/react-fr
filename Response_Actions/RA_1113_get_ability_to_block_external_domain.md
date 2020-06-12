| Title                       | Avoir la possibilité de bloquer un domaine externe        |
|:---------------------------:|:--------------------|
| **ID**                      | RA1113            |
| **Description**             | Assurez-vous que vous avez la possibilité d'empêcher l'accès à un nom de domaine externe par les actifs de l'entreprise   |
| **Author**                  | @atc_project -  Traduit et Mise à jour par Crypt-0n     |
| **Creation Date**           | 06.05.2020 |
| **Category**                | Réseau      |
| **Stage**                   |[RS0001: Preparation](../Response_Stages/RS0001.md)| 
| **References** |<ul><li>[https://en.wikipedia.org/wiki/DNS_sinkhole](https://en.wikipedia.org/wiki/DNS_sinkhole)</li></ul>|
| **Requirements** |<ul><li>MS_border_proxy</li><li>MS_border_ips</li><li>MS_border_ngfw</li><li>MS_dns_server</li></ul>|

### Workflow

Assurez-vous que vous avez la possibilité de créer une règle de stratégie ou une configuration spécifique dans l'un des systèmes d'atténuation répertoriés qui vous empêchera l'accès à un nom de domaine externe par les actifs de l'entreprise.

Warning:  

- Assurez-vous qu'en utilisant les systèmes répertoriés (1 ou plusieurs), vous pouvez contrôler l'accès à Internet de tous les actifs de l'infrastructure. Dans certains cas, vous aurez besoin d'un moyen garanti d'empêcher complètement l'accès à un nom de domaine externe par les actifs de l'entreprise. Si certains actifs ne sont pas sous la gestion des systèmes d'atténuation répertoriés (afin qu'ils puissent accéder à Internet en contournant ces systèmes), vous ne pourrez pas atteindre pleinement l'objectif final de la mesure.
