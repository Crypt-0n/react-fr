| Title                       | Accéder aux journaux DNS externes         |
|:---------------------------:|:--------------------|
| **ID**                      | RA1106            |
| **Description**             | Assurez-vous d'avoir accès aux journaux DNS des communications externes   |
| **Author**                  | @atc_project - Traduit et Mise à jour par Crypt-0n       |
| **Creation Date**           | 11.06.2020 |
| **Category**                | Réseau      |
| **Stage**                   |[RS0001: Preparation](../Response_Stages/RS0001.md)| 
| **References** |<ul><li>[https://github.com/gamelinux/passivedns](https://github.com/gamelinux/passivedns)</li><li>[https://drive.google.com/drive/u/0/folders/0B5BuM3k0_mF3LXpnYVUtU091Vjg](https://drive.google.com/drive/u/0/folders/0B5BuM3k0_mF3LXpnYVUtU091Vjg)</li></ul>|
| **Requirements** |<ul><li>MS_dns_server</li><li>DN_zeek_dns_log</li></ul>|

### Workflow

Assurez-vous qu'il existe une collecte de journaux DNS pour la communication externe (des actifs de l'entreprise à Internet) configurée.
S'il n'y a pas d'option pour le configurer sur un périphérique réseau / serveur DNS, vous pouvez installer un logiciel spécial sur chaque point de terminaison et le collecter à partir d'eux. 

Warning:  

- Assurez-vous que des journaux de requêtes et de réponses DNS sont collectés. Il est assez difficile de configurer une telle collection sur le serveur DNS MS Windows et ISC BIND. Parfois, il est beaucoup plus facile d'utiliser des solutions tierces pour répondre à cette exigence.
- Assurez-vous que le trafic DNS vers les serveurs DNS externes (publics) est bloqué par le pare-feu de Bordure. De cette façon, les serveurs DNS d'entreprise sont le seul endroit où les actifs peuvent résoudre les noms de domaine.
