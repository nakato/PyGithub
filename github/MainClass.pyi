from datetime import datetime
from io import BytesIO
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union

from github.AuthenticatedUser import AuthenticatedUser
from github.Commit import Commit
from github.ContentFile import ContentFile
from github.Event import Event
from github.Gist import Gist
from github.GithubObject import GithubObject, _NotSetType
from github.GitignoreTemplate import GitignoreTemplate
from github.HookDescription import HookDescription
from github.Installation import Installation
from github.InstallationAuthorization import InstallationAuthorization
from github.Issue import Issue
from github.License import License
from github.NamedUser import NamedUser
from github.Organization import Organization
from github.PaginatedList import PaginatedList
from github.Project import Project
from github.RateLimit import RateLimit
from github.Repository import Repository
from github.Topic import Topic

# from urllib3.util.retry import Retry

TGithubObject = TypeVar('TGithubObject', bound=GithubObject)

class Github:
    def __init__(
        self,
        login_or_token: Optional[str] = ...,
        password: Optional[str] = ...,
        jwt: Optional[str] = ...,
        base_url: str = ...,
        timeout: int = ...,
        client_id: Optional[str] = ...,
        client_secret: Optional[str] = ...,
        user_agent: str = ...,
        per_page: int = ...,
        verify: bool = ...,
        retry: Any = ...,
    ) -> None: ...
    def __get_FIX_REPO_GET_GIT_REF(self) -> bool: ...
    def __set_FIX_REPO_GET_GIT_REF(self, value: bool) -> None: ...
    def __get_per_page(self) -> int: ...
    def __set_per_page(self, value: int) -> None: ...
    def create_from_raw_data(
        self,
        klass: Type[TGithubObject],
        raw_data: Dict[str, Any],
        headers: Dict[str, Union[str, int]] = ...,
    ) -> TGithubObject: ...
    def dump(self, obj: GithubObject, file: BytesIO, protocol: int = ...) -> None: ...
    def get_emojis(self) -> Dict[str, str]: ...
    def get_events(self) -> PaginatedList[Event]: ...
    def get_gist(self, id: str) -> Gist: ...
    def get_gists(
        self, since: Union[datetime, _NotSetType] = ...
    ) -> PaginatedList[Gist]: ...
    def get_gitignore_template(self, name: str) -> GitignoreTemplate: ...
    def get_gitignore_templates(self) -> List[str]: ...
    def get_hook(self, name: str) -> HookDescription: ...
    def get_hooks(self) -> List[HookDescription]: ...
    def get_installation(self, id: int) -> Installation: ...
    def get_license(self, key: Union[str, _NotSetType] = ...) -> License: ...
    def get_licenses(self) -> PaginatedList[License]: ...
    def get_organization(self, login: str) -> Organization: ...
    def get_organizations(
        self, since: Union[int, _NotSetType] = ...
    ) -> PaginatedList[Organization]: ...
    def get_project(self, id: int) -> Project: ...
    def get_rate_limit(self) -> RateLimit: ...
    def get_repo(
        self, full_name_or_id: Union[int, str], lazy: bool = ...
    ) -> Repository: ...
    def get_repos(
        self,
        since: Union[int, _NotSetType] = ...,
        visibility: Union[str, _NotSetType] = ...,
    ) -> PaginatedList[Repository]: ...
    def get_user(
        self, login: Union[str, _NotSetType] = ...
    ) -> Union[AuthenticatedUser, NamedUser]: ...
    def get_users(
        self, since: Union[int, _NotSetType] = ...
    ) -> PaginatedList[NamedUser]: ...
    def load(self, f: BytesIO) -> Repository: ...
    @property
    def oauth_scopes(self) -> Optional[List[str]]: ...
    @property
    def rate_limiting(self) -> Tuple[int, int]: ...
    @property
    def rate_limiting_resettime(self) -> int: ...
    def render_markdown(
        self, text: str, context: Union[Repository, _NotSetType] = ...
    ) -> str: ...
    def search_code(
        self,
        query: str,
        sort: Union[str, _NotSetType] = ...,
        order: Union[str, _NotSetType] = ...,
        highlight: bool = ...,
        **qualifiers: Dict[str, Any]
    ) -> PaginatedList[ContentFile]: ...
    def search_commits(
        self,
        query: str,
        sort: Union[str, _NotSetType] = ...,
        order: Union[str, _NotSetType] = ...,
        **qualifiers: Dict[str, Any]
    ) -> PaginatedList[Commit]: ...
    def search_issues(
        self,
        query: str,
        sort: Union[str, _NotSetType] = ...,
        order: Union[str, _NotSetType] = ...,
        **qualifiers: Dict[str, Any]
    ) -> PaginatedList[Issue]: ...
    def search_repositories(
        self,
        query: str,
        sort: Union[str, _NotSetType] = ...,
        order: Union[str, _NotSetType] = ...,
        **qualifiers: Dict[str, Any]
    ) -> PaginatedList[Repository]: ...
    def search_topics(
        self,
        query: str,
        **qualifiers: Dict[str, Any]
    ) -> PaginatedList[Topic]: ...
    def search_users(
        self,
        query: str,
        sort: Union[str, _NotSetType] = ...,
        order: Union[str, _NotSetType] = ...,
        **qualifiers: Dict[str, Any]
    ) -> PaginatedList[NamedUser]: ...

class GithubIntegration:
    def __init__(
        self, integration_id: Union[int, str], private_key: str, base_url: str = ...
    ) -> None: ...
    def create_jwt(self, expiration: int = ...) -> str: ...
    def get_access_token(
        self, installation_id: int, user_id: Optional[int] = ...
    ) -> InstallationAuthorization: ...
    def get_installation(self, owner: str, repo: str) -> Installation: ...
