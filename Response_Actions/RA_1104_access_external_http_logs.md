| Title                       | Accéder aux journaux HTTP externes         |
|:---------------------------:|:--------------------|
| **ID**                      | RA1104            |
| **Description**             | Assurez-vous d'avoir accès aux journaux HTTP de communication externe   |
| **Author**                  | @atc_project - Traduit et Mise à jour par Crypt-0n       |
| **Creation Date**           | 11.06.2020 |
| **Category**                | Réseau      |
| **Stage**                   |[RS0001: Preparation](../Response_Stages/RS0001.md)| 
| **References** |<ul><li>[https://docs.zeek.org/en/current/examples/httpmonitor/](https://docs.zeek.org/en/current/examples/httpmonitor/)</li><li>[https://en.wikipedia.org/wiki/Common_Log_Format](https://en.wikipedia.org/wiki/Common_Log_Format)</li></ul>|
| **Requirements** |<ul><li>MS_border_proxy</li><li>MS_border_ngfw</li><li>DN_zeek_http_log</li></ul>|

### Workflow

Assurez-vous qu'il existe une collection de journaux de connexions HTTP pour la communication externe (des actifs de l'entreprise à Internet) configurée
