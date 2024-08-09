"""Generated message classes for gsuiteaddons version v1.

"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'gsuiteaddons'


class GoogleAppsScriptTypeAddOnWidgetSet(_messages.Message):
  r"""The widget subset used by an add-on.

  Enums:
    UsedWidgetsValueListEntryValuesEnum:

  Fields:
    usedWidgets: The list of widgets used in an add-on.
  """

  class UsedWidgetsValueListEntryValuesEnum(_messages.Enum):
    r"""UsedWidgetsValueListEntryValuesEnum enum type.

    Values:
      WIDGET_TYPE_UNSPECIFIED: The default widget set.
      DATE_PICKER: The date picker.
      STYLED_BUTTONS: Styled buttons include filled buttons and deactivated
        buttons.
      PERSISTENT_FORMS: Persistent forms allow persisting form values during
        actions.
      FIXED_FOOTER: Fixed footer in a card.
      UPDATE_SUBJECT_AND_RECIPIENTS: Update the subject and recipients of a
        draft.
      GRID_WIDGET: The grid widget.
      ADDON_COMPOSE_UI_ACTION: A Gmail add-on action that applies to the add-
        on compose UI.
    """
    WIDGET_TYPE_UNSPECIFIED = 0
    DATE_PICKER = 1
    STYLED_BUTTONS = 2
    PERSISTENT_FORMS = 3
    FIXED_FOOTER = 4
    UPDATE_SUBJECT_AND_RECIPIENTS = 5
    GRID_WIDGET = 6
    ADDON_COMPOSE_UI_ACTION = 7

  usedWidgets = _messages.EnumField('UsedWidgetsValueListEntryValuesEnum', 1, repeated=True)


class GoogleAppsScriptTypeCalendarCalendarAddOnManifest(_messages.Message):
  r"""Properties customizing the appearance and execution of a Calendar add-
  on.

  Enums:
    CurrentEventAccessValueValuesEnum: Defines the level of data access when
      an event add-on is triggered.

  Fields:
    conferenceSolution: Defines conference solutions provided by this add-on.
    createSettingsUrlFunction: An endpoint to execute that creates a URL to
      the add-on's settings page.
    currentEventAccess: Defines the level of data access when an event add-on
      is triggered.
    eventAttachmentTrigger: An endpoint that triggers when the event add-
      attachment flow is selected. Add-ons that declare this endpoint will be
      considered as an attachment provider.
    eventOpenTrigger: An endpoint that triggers when an event is opened to be
      viewed or edited.
    eventUpdateTrigger: An endpoint that triggers when the open event is
      updated.
    homepageTrigger: Defines an endpoint that is executed in contexts that
      don't match a declared contextual trigger. Any cards generated by this
      function will always be available to the user, but might be eclipsed by
      contextual content when this add-on declares more targeted triggers. If
      present, this overrides the configuration from
      `addOns.common.homepageTrigger`.
  """

  class CurrentEventAccessValueValuesEnum(_messages.Enum):
    r"""Defines the level of data access when an event add-on is triggered.

    Values:
      UNSPECIFIED: Default value when nothing is set for eventAccess.
      METADATA: Gives event triggers the permission to access the metadata of
        events, such as event ID and calendar ID.
      READ: Gives event triggers access to all provided event fields including
        the metadata, attendees, and conference data.
      WRITE: Gives event triggers access to the metadata of events and the
        ability to perform all actions, including adding attendees and setting
        conference data.
      READ_WRITE: Gives event triggers access to all provided event fields
        including the metadata, attendees, and conference data and the ability
        to perform all actions.
    """
    UNSPECIFIED = 0
    METADATA = 1
    READ = 2
    WRITE = 3
    READ_WRITE = 4

  conferenceSolution = _messages.MessageField('GoogleAppsScriptTypeCalendarConferenceSolution', 1, repeated=True)
  createSettingsUrlFunction = _messages.StringField(2)
  currentEventAccess = _messages.EnumField('CurrentEventAccessValueValuesEnum', 3)
  eventAttachmentTrigger = _messages.MessageField('GoogleAppsScriptTypeMenuItemExtensionPoint', 4)
  eventOpenTrigger = _messages.MessageField('GoogleAppsScriptTypeCalendarCalendarExtensionPoint', 5)
  eventUpdateTrigger = _messages.MessageField('GoogleAppsScriptTypeCalendarCalendarExtensionPoint', 6)
  homepageTrigger = _messages.MessageField('GoogleAppsScriptTypeHomepageExtensionPoint', 7)


class GoogleAppsScriptTypeCalendarCalendarExtensionPoint(_messages.Message):
  r"""Common format for declaring a calendar add-on's triggers.

  Fields:
    runFunction: Required. The endpoint to execute when this extension point
      is activated.
  """

  runFunction = _messages.StringField(1)


class GoogleAppsScriptTypeCalendarConferenceSolution(_messages.Message):
  r"""Defines conference related values.

  Fields:
    id: Required. IDs should be uniquely assigned across conference solutions
      within one add-on, otherwise the wrong conference solution might be used
      when the add-on is triggered. While you can change the display name of
      an add-on, the ID shouldn't be changed.
    logoUrl: Required. The URL for the logo image of the conference solution.
    name: Required. The display name of the conference solution.
    onCreateFunction: Required. The endpoint to call when conference data
      should be created.
  """

  id = _messages.StringField(1)
  logoUrl = _messages.StringField(2)
  name = _messages.StringField(3)
  onCreateFunction = _messages.StringField(4)


class GoogleAppsScriptTypeCommonAddOnManifest(_messages.Message):
  r"""Add-on configuration that is shared across all add-on host applications.

  Fields:
    addOnWidgetSet: The widgets used in the add-on. If this field is not
      specified, the default set is used.
    homepageTrigger: Defines an endpoint that will be executed in any context,
      in any host. Any cards generated by this function will always be
      available to the user, but might be eclipsed by contextual content when
      this add-on declares more targeted triggers.
    layoutProperties: Common layout properties for the add-on cards.
    logoUrl: Required. The URL for the logo image shown in the add-on toolbar.
    name: Required. The display name of the add-on.
    openLinkUrlPrefixes: An OpenLink action can only use a URL with an
      `HTTPS`, `MAILTO` or `TEL` scheme. For `HTTPS` links, the URL must also
      [match](/gmail/add-ons/concepts/manifests#whitelisting_urls) one of the
      prefixes specified in the allowlist. If the prefix omits the scheme,
      `HTTPS` is assumed. `HTTP` links are automatically rewritten to `HTTPS`
      links.
    universalActions: Defines a list of extension points in the universal
      action menu which serves as a settings menu for the add-on. The
      extension point can be a link URL to open or an endpoint to execute as a
      form submission.
    useLocaleFromApp: Whether to pass locale information from host app.
  """

  addOnWidgetSet = _messages.MessageField('GoogleAppsScriptTypeAddOnWidgetSet', 1)
  homepageTrigger = _messages.MessageField('GoogleAppsScriptTypeHomepageExtensionPoint', 2)
  layoutProperties = _messages.MessageField('GoogleAppsScriptTypeLayoutProperties', 3)
  logoUrl = _messages.StringField(4)
  name = _messages.StringField(5)
  openLinkUrlPrefixes = _messages.MessageField('extra_types.JsonValue', 6, repeated=True)
  universalActions = _messages.MessageField('GoogleAppsScriptTypeUniversalActionExtensionPoint', 7, repeated=True)
  useLocaleFromApp = _messages.BooleanField(8)


class GoogleAppsScriptTypeDocsDocsAddOnManifest(_messages.Message):
  r"""Properties customizing the appearance and execution of a Google Docs
  add-on.

  Fields:
    homepageTrigger: If present, this overrides the configuration from
      `addOns.common.homepageTrigger`.
    linkPreviewTriggers: A list of extension points for previewing links in a
      Google Docs document. For details, see [Preview links with smart
      chips](https://developers.google.com/workspace/add-ons/guides/preview-
      links-smart-chips).
    onFileScopeGrantedTrigger: Endpoint to execute when file scope
      authorization is granted for this document/user pair.
  """

  homepageTrigger = _messages.MessageField('GoogleAppsScriptTypeHomepageExtensionPoint', 1)
  linkPreviewTriggers = _messages.MessageField('GoogleAppsScriptTypeLinkPreviewExtensionPoint', 2, repeated=True)
  onFileScopeGrantedTrigger = _messages.MessageField('GoogleAppsScriptTypeDocsDocsExtensionPoint', 3)


class GoogleAppsScriptTypeDocsDocsExtensionPoint(_messages.Message):
  r"""Common format for declaring a Docs add-on's triggers.

  Fields:
    runFunction: Required. The endpoint to execute when this extension point
      is activated.
  """

  runFunction = _messages.StringField(1)


class GoogleAppsScriptTypeDriveDriveAddOnManifest(_messages.Message):
  r"""Properties customizing the appearance and execution of a Drive add-on.

  Fields:
    homepageTrigger: If present, this overrides the configuration from
      `addOns.common.homepageTrigger`.
    onItemsSelectedTrigger: Corresponds to behavior that executes when items
      are selected in the relevant Drive view, such as the My Drive Doclist.
  """

  homepageTrigger = _messages.MessageField('GoogleAppsScriptTypeHomepageExtensionPoint', 1)
  onItemsSelectedTrigger = _messages.MessageField('GoogleAppsScriptTypeDriveDriveExtensionPoint', 2)


class GoogleAppsScriptTypeDriveDriveExtensionPoint(_messages.Message):
  r"""Common format for declaring a Drive add-on's triggers.

  Fields:
    runFunction: Required. The endpoint to execute when the extension point is
      activated.
  """

  runFunction = _messages.StringField(1)


class GoogleAppsScriptTypeGmailComposeTrigger(_messages.Message):
  r"""A trigger that activates when user is composing an email.

  Enums:
    DraftAccessValueValuesEnum: Defines the level of data access when a
      compose time add-on is triggered.

  Fields:
    actions: Defines the set of actions for a compose time add-on. These are
      actions that users can trigger on a compose time add-on.
    draftAccess: Defines the level of data access when a compose time add-on
      is triggered.
  """

  class DraftAccessValueValuesEnum(_messages.Enum):
    r"""Defines the level of data access when a compose time add-on is
    triggered.

    Values:
      UNSPECIFIED: Default value when nothing is set for draftAccess.
      NONE: The compose trigger can't access any data of the draft when a
        compose add-on is triggered.
      METADATA: Gives the compose trigger the permission to access the
        metadata of the draft when a compose add-on is triggered. This
        includes the audience list, such as the To and Cc list of a draft
        message.
    """
    UNSPECIFIED = 0
    NONE = 1
    METADATA = 2

  actions = _messages.MessageField('GoogleAppsScriptTypeMenuItemExtensionPoint', 1, repeated=True)
  draftAccess = _messages.EnumField('DraftAccessValueValuesEnum', 2)


class GoogleAppsScriptTypeGmailContextualTrigger(_messages.Message):
  r"""Defines a trigger that fires when the open email meets a specific
  criteria. When the trigger fires, it executes a specific endpoint, usually
  in order to create new cards and update the UI.

  Fields:
    onTriggerFunction: Required. The name of the endpoint to call when a
      message matches the trigger.
    unconditional: Unconditional triggers are executed when any mail message
      is opened.
  """

  onTriggerFunction = _messages.StringField(1)
  unconditional = _messages.MessageField('GoogleAppsScriptTypeGmailUnconditionalTrigger', 2)


class GoogleAppsScriptTypeGmailGmailAddOnManifest(_messages.Message):
  r"""Properties customizing the appearance and execution of a Gmail add-on.

  Fields:
    authorizationCheckFunction: The name of an endpoint that verifies that the
      add-on has all the required third-party authorizations, by probing the
      third-party APIs. If the probe fails, the function should throw an
      exception to initiate the authorization flow. This function is called
      before each invocation of the add-on in order to ensure a smooth user
      experience.
    composeTrigger: Defines the compose time trigger for a compose time add-
      on. This is the trigger that causes an add-on to take action when the
      user is composing an email. All compose time add-ons must have the
      `gmail.addons.current.action.compose` scope even though it might not
      edit the draft.
    contextualTriggers: Defines the set of conditions that trigger the add-on.
    homepageTrigger: Defines an endpoint that will be executed in contexts
      that don't match a declared contextual trigger. Any cards generated by
      this function will always be available to the user, but may be eclipsed
      by contextual content when this add-on declares more targeted triggers.
      If present, this overrides the configuration from
      `addOns.common.homepageTrigger`.
    universalActions: Defines a set of [universal actions](/gmail/add-ons/how-
      tos/universal-actions) for the add-on. The user triggers universal
      actions from the add-on toolbar menu.
  """

  authorizationCheckFunction = _messages.StringField(1)
  composeTrigger = _messages.MessageField('GoogleAppsScriptTypeGmailComposeTrigger', 2)
  contextualTriggers = _messages.MessageField('GoogleAppsScriptTypeGmailContextualTrigger', 3, repeated=True)
  homepageTrigger = _messages.MessageField('GoogleAppsScriptTypeHomepageExtensionPoint', 4)
  universalActions = _messages.MessageField('GoogleAppsScriptTypeGmailUniversalAction', 5, repeated=True)


class GoogleAppsScriptTypeGmailUnconditionalTrigger(_messages.Message):
  r"""A trigger that fires when any email message is opened."""


class GoogleAppsScriptTypeGmailUniversalAction(_messages.Message):
  r"""An action that is always available in the add-on toolbar menu regardless
  of message context.

  Fields:
    openLink: A link that is opened by Gmail when the user triggers the
      action.
    runFunction: An endpoint that is called when the user triggers the action.
      See the [universal actions guide](/gmail/add-ons/how-tos/universal-
      actions) for details.
    text: Required. User-visible text describing the action, for example, "Add
      a new contact."
  """

  openLink = _messages.StringField(1)
  runFunction = _messages.StringField(2)
  text = _messages.StringField(3)


class GoogleAppsScriptTypeHomepageExtensionPoint(_messages.Message):
  r"""Common format for declaring an add-on's homepage view.

  Fields:
    enabled: Optional. If set to `false`, deactivates the homepage view in
      this context. Defaults to `true` if unset. If an add-on's custom
      homepage view is disabled, a generic overview card is provided for users
      instead.
    runFunction: Required. The endpoint to execute when this extension point
      is activated.
  """

  enabled = _messages.BooleanField(1)
  runFunction = _messages.StringField(2)


class GoogleAppsScriptTypeHttpOptions(_messages.Message):
  r"""Options for sending requests to add-on `HTTP` endpoints.

  Enums:
    AuthorizationHeaderValueValuesEnum: Configuration for the token sent in
      the `HTTP` Authorization header.

  Fields:
    authorizationHeader: Configuration for the token sent in the `HTTP`
      Authorization header.
  """

  class AuthorizationHeaderValueValuesEnum(_messages.Enum):
    r"""Configuration for the token sent in the `HTTP` Authorization header.

    Values:
      HTTP_AUTHORIZATION_HEADER_UNSPECIFIED: Default value, equivalent to
        `SYSTEM_ID_TOKEN`.
      SYSTEM_ID_TOKEN: Send an ID token for the project-specific Google
        Workspace Add-on's system service account (default).
      USER_ID_TOKEN: Send an ID token for the end user.
      NONE: Do not send an Authentication header.
    """
    HTTP_AUTHORIZATION_HEADER_UNSPECIFIED = 0
    SYSTEM_ID_TOKEN = 1
    USER_ID_TOKEN = 2
    NONE = 3

  authorizationHeader = _messages.EnumField('AuthorizationHeaderValueValuesEnum', 1)


class GoogleAppsScriptTypeLayoutProperties(_messages.Message):
  r"""Card layout properties shared across all add-on host applications.

  Fields:
    primaryColor: The primary color of the add-on. It sets the color of the
      toolbar. If no primary color is set, the default value provided by the
      framework is used.
    secondaryColor: The secondary color of the add-on. It sets the color of
      buttons. If the primary color is set but no secondary color is set, the
      secondary color is the same as the primary color. If neither primary
      color nor secondary color is set, the default value provided by the
      framework is used.
    useNewMaterialDesign: Enables material design for cards.
  """

  primaryColor = _messages.StringField(1)
  secondaryColor = _messages.StringField(2)
  useNewMaterialDesign = _messages.BooleanField(3)


class GoogleAppsScriptTypeLinkPreviewExtensionPoint(_messages.Message):
  r"""The configuration for a trigger that fires when a user types or pastes a
  link from a third-party or non-Google service into a Google Docs, Sheets, or
  Slides file.

  Messages:
    LocalizedLabelTextValue: Optional. A map of `labelText` to localize into
      other languages. Format the language in [ISO
      639](https://wikipedia.org/wiki/ISO_639_macrolanguage) and the
      country/region in [ISO 3166](https://wikipedia.org/wiki/ISO_3166),
      separated by a hyphen `-`. For example, `en-US`. If a user's locale is
      present in the map's keys, the user sees the localized version of the
      `labelText`.

  Fields:
    labelText: Required. The text for an example smart chip that prompts users
      to preview the link, such as `Example: Support case`. This text is
      static and displays before users execute the add-on.
    localizedLabelText: Optional. A map of `labelText` to localize into other
      languages. Format the language in [ISO
      639](https://wikipedia.org/wiki/ISO_639_macrolanguage) and the
      country/region in [ISO 3166](https://wikipedia.org/wiki/ISO_3166),
      separated by a hyphen `-`. For example, `en-US`. If a user's locale is
      present in the map's keys, the user sees the localized version of the
      `labelText`.
    logoUrl: Optional. The icon that displays in the smart chip and preview
      card. If omitted, the add-on uses its toolbar icon,
      [`logoUrl`](https://developers.google.com/workspace/add-ons/reference/re
      st/v1/projects.deployments#CommonAddOnManifest.FIELDS.logoUrl).
    patterns: Required. An array of URL patterns that trigger the add-on to
      preview links.
    runFunction: Required. Endpoint to execute when a link preview is
      triggered.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LocalizedLabelTextValue(_messages.Message):
    r"""Optional. A map of `labelText` to localize into other languages.
    Format the language in [ISO
    639](https://wikipedia.org/wiki/ISO_639_macrolanguage) and the
    country/region in [ISO 3166](https://wikipedia.org/wiki/ISO_3166),
    separated by a hyphen `-`. For example, `en-US`. If a user's locale is
    present in the map's keys, the user sees the localized version of the
    `labelText`.

    Messages:
      AdditionalProperty: An additional property for a LocalizedLabelTextValue
        object.

    Fields:
      additionalProperties: Additional properties of type
        LocalizedLabelTextValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LocalizedLabelTextValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  labelText = _messages.StringField(1)
  localizedLabelText = _messages.MessageField('LocalizedLabelTextValue', 2)
  logoUrl = _messages.StringField(3)
  patterns = _messages.MessageField('GoogleAppsScriptTypeUriPattern', 4, repeated=True)
  runFunction = _messages.StringField(5)


class GoogleAppsScriptTypeMenuItemExtensionPoint(_messages.Message):
  r"""Common format for declaring a menu item or button that appears within a
  host app.

  Fields:
    label: Required. User-visible text that describes the action taken by
      activating this extension point. For example, "Insert invoice."
    logoUrl: The URL for the logo image shown in the add-on toolbar. If not
      set, defaults to the add-on's primary logo URL.
    runFunction: Required. The endpoint to execute when this extension point
      is activated.
  """

  label = _messages.StringField(1)
  logoUrl = _messages.StringField(2)
  runFunction = _messages.StringField(3)


class GoogleAppsScriptTypeSheetsSheetsAddOnManifest(_messages.Message):
  r"""Properties customizing the appearance and execution of a Google Sheets
  add-on.

  Fields:
    homepageTrigger: If present, this overrides the configuration from
      `addOns.common.homepageTrigger`.
    linkPreviewTriggers: A list of extension points for previewing links in a
      Google Sheets document. For details, see [Preview links with smart
      chips](https://developers.google.com/workspace/add-ons/guides/preview-
      links-smart-chips).
    onFileScopeGrantedTrigger: Endpoint to execute when file scope
      authorization is granted for this document/user pair.
  """

  homepageTrigger = _messages.MessageField('GoogleAppsScriptTypeHomepageExtensionPoint', 1)
  linkPreviewTriggers = _messages.MessageField('GoogleAppsScriptTypeLinkPreviewExtensionPoint', 2, repeated=True)
  onFileScopeGrantedTrigger = _messages.MessageField('GoogleAppsScriptTypeSheetsSheetsExtensionPoint', 3)


class GoogleAppsScriptTypeSheetsSheetsExtensionPoint(_messages.Message):
  r"""Common format for declaring a Sheets add-on's triggers.

  Fields:
    runFunction: Required. The endpoint to execute when this extension point
      is activated.
  """

  runFunction = _messages.StringField(1)


class GoogleAppsScriptTypeSlidesSlidesAddOnManifest(_messages.Message):
  r"""Properties customizing the appearance and execution of a Google Slides
  add-on.

  Fields:
    homepageTrigger: If present, this overrides the configuration from
      `addOns.common.homepageTrigger`.
    linkPreviewTriggers: A list of extension points for previewing links in a
      Google Slides document. For details, see [Preview links with smart
      chips](https://developers.google.com/workspace/add-ons/guides/preview-
      links-smart-chips).
    onFileScopeGrantedTrigger: Endpoint to execute when file scope
      authorization is granted for this document/user pair.
  """

  homepageTrigger = _messages.MessageField('GoogleAppsScriptTypeHomepageExtensionPoint', 1)
  linkPreviewTriggers = _messages.MessageField('GoogleAppsScriptTypeLinkPreviewExtensionPoint', 2, repeated=True)
  onFileScopeGrantedTrigger = _messages.MessageField('GoogleAppsScriptTypeSlidesSlidesExtensionPoint', 3)


class GoogleAppsScriptTypeSlidesSlidesExtensionPoint(_messages.Message):
  r"""Common format for declaring a Slides add-on's triggers.

  Fields:
    runFunction: Required. The endpoint to execute when this extension point
      is activated.
  """

  runFunction = _messages.StringField(1)


class GoogleAppsScriptTypeUniversalActionExtensionPoint(_messages.Message):
  r"""Format for declaring a universal action menu item extension point.

  Fields:
    label: Required. User-visible text that describes the action taken by
      activating this extension point, for example, "Add a new contact."
    openLink: URL to be opened by the UniversalAction.
    runFunction: Endpoint to be run by the UniversalAction.
  """

  label = _messages.StringField(1)
  openLink = _messages.StringField(2)
  runFunction = _messages.StringField(3)


class GoogleAppsScriptTypeUriPattern(_messages.Message):
  r"""The configuration for each URL pattern that triggers a link preview.

  Fields:
    hostPattern: Required for each URL pattern to preview. The domain of the
      URL pattern. The add-on previews links that contain this domain in the
      URL. To preview links for a specific subdomain, like
      `subdomain.example.com`, include the subdomain. To preview links for the
      entire domain, specify a wildcard character with an asterisk (`*`) as
      the subdomain. For example, `*.example.com` matches
      `subdomain.example.com` and `another.subdomain.example.com`.
    pathPrefix: Optional. The path that appends the domain of the
      `hostPattern`. For example, if the URL host pattern is
      `support.example.com`, to match URLs for cases hosted at
      `support.example.com/cases/`, enter `cases`. To match all URLs in the
      host pattern domain, leave `pathPrefix` empty.
  """

  hostPattern = _messages.StringField(1)
  pathPrefix = _messages.StringField(2)


class GoogleCloudGsuiteaddonsV1AddOns(_messages.Message):
  r"""A Google Workspace Add-on configuration.

  Fields:
    calendar: Calendar add-on configuration.
    common: Configuration that is common across all Google Workspace Add-ons.
    docs: Docs add-on configuration.
    drive: Drive add-on configuration.
    gmail: Gmail add-on configuration.
    httpOptions: Options for sending requests to add-on HTTP endpoints
    sheets: Sheets add-on configuration.
    slides: Slides add-on configuration.
  """

  calendar = _messages.MessageField('GoogleAppsScriptTypeCalendarCalendarAddOnManifest', 1)
  common = _messages.MessageField('GoogleAppsScriptTypeCommonAddOnManifest', 2)
  docs = _messages.MessageField('GoogleAppsScriptTypeDocsDocsAddOnManifest', 3)
  drive = _messages.MessageField('GoogleAppsScriptTypeDriveDriveAddOnManifest', 4)
  gmail = _messages.MessageField('GoogleAppsScriptTypeGmailGmailAddOnManifest', 5)
  httpOptions = _messages.MessageField('GoogleAppsScriptTypeHttpOptions', 6)
  sheets = _messages.MessageField('GoogleAppsScriptTypeSheetsSheetsAddOnManifest', 7)
  slides = _messages.MessageField('GoogleAppsScriptTypeSlidesSlidesAddOnManifest', 8)


class GoogleCloudGsuiteaddonsV1Authorization(_messages.Message):
  r"""The authorization information used when invoking deployment endpoints.

  Fields:
    name: The canonical full name of this resource. Example:
      `projects/123/authorization`
    oauthClientId: The OAuth client ID used to obtain OAuth access tokens for
      a user on the add-on's behalf.
    serviceAccountEmail: The email address of the service account used to
      authenticate requests to add-on callback endpoints.
  """

  name = _messages.StringField(1)
  oauthClientId = _messages.StringField(2)
  serviceAccountEmail = _messages.StringField(3)


class GoogleCloudGsuiteaddonsV1Deployment(_messages.Message):
  r"""A Google Workspace Add-on deployment

  Fields:
    addOns: The Google Workspace Add-on configuration.
    etag: This value is computed by the server based on the version of the
      deployment in storage, and may be sent on update and delete requests to
      ensure the client has an up-to-date value before proceeding.
    name: The deployment resource name. Example:
      `projects/123/deployments/my_deployment`.
    oauthScopes: The list of Google OAuth scopes for which to request consent
      from the end user before executing an add-on endpoint.
  """

  addOns = _messages.MessageField('GoogleCloudGsuiteaddonsV1AddOns', 1)
  etag = _messages.StringField(2)
  name = _messages.StringField(3)
  oauthScopes = _messages.StringField(4, repeated=True)


class GoogleCloudGsuiteaddonsV1InstallDeploymentRequest(_messages.Message):
  r"""Request message to install a deployment for testing."""


class GoogleCloudGsuiteaddonsV1InstallStatus(_messages.Message):
  r"""Install status of a test deployment.

  Fields:
    installed: True if the deployment is installed for the user.
    name: The canonical full resource name of the deployment install status.
      Example: `projects/123/deployments/my_deployment/installStatus`.
  """

  installed = _messages.BooleanField(1)
  name = _messages.StringField(2)


class GoogleCloudGsuiteaddonsV1ListDeploymentsResponse(_messages.Message):
  r"""Response message to list deployments.

  Fields:
    deployments: The list of deployments for the given project.
    nextPageToken: A token, which can be sent as `page_token` to retrieve the
      next page. If this field is omitted, there are no subsequent pages.
  """

  deployments = _messages.MessageField('GoogleCloudGsuiteaddonsV1Deployment', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class GoogleCloudGsuiteaddonsV1UninstallDeploymentRequest(_messages.Message):
  r"""Request message to uninstall a test deployment."""


class GoogleProtobufEmpty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance: service Foo { rpc
  Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }
  """



class GsuiteaddonsProjectsDeploymentsCreateRequest(_messages.Message):
  r"""A GsuiteaddonsProjectsDeploymentsCreateRequest object.

  Fields:
    deploymentId: Required. The ID to use for this deployment. The full name
      of the created resource will be `projects//deployments/`.
    googleCloudGsuiteaddonsV1Deployment: A GoogleCloudGsuiteaddonsV1Deployment
      resource to be passed as the request body.
    parent: Required. Name of the project in which to create the deployment.
      Example: `projects/my_project`.
  """

  deploymentId = _messages.StringField(1)
  googleCloudGsuiteaddonsV1Deployment = _messages.MessageField('GoogleCloudGsuiteaddonsV1Deployment', 2)
  parent = _messages.StringField(3, required=True)


class GsuiteaddonsProjectsDeploymentsDeleteRequest(_messages.Message):
  r"""A GsuiteaddonsProjectsDeploymentsDeleteRequest object.

  Fields:
    etag: The etag of the deployment to delete. If this is provided, it must
      match the server's etag.
    name: Required. The full resource name of the deployment to delete.
      Example: `projects/my_project/deployments/my_deployment`.
  """

  etag = _messages.StringField(1)
  name = _messages.StringField(2, required=True)


class GsuiteaddonsProjectsDeploymentsGetInstallStatusRequest(_messages.Message):
  r"""A GsuiteaddonsProjectsDeploymentsGetInstallStatusRequest object.

  Fields:
    name: Required. The full resource name of the deployment. Example:
      `projects/my_project/deployments/my_deployment/installStatus`.
  """

  name = _messages.StringField(1, required=True)


class GsuiteaddonsProjectsDeploymentsGetRequest(_messages.Message):
  r"""A GsuiteaddonsProjectsDeploymentsGetRequest object.

  Fields:
    name: Required. The full resource name of the deployment to get. Example:
      `projects/my_project/deployments/my_deployment`.
  """

  name = _messages.StringField(1, required=True)


class GsuiteaddonsProjectsDeploymentsInstallRequest(_messages.Message):
  r"""A GsuiteaddonsProjectsDeploymentsInstallRequest object.

  Fields:
    googleCloudGsuiteaddonsV1InstallDeploymentRequest: A
      GoogleCloudGsuiteaddonsV1InstallDeploymentRequest resource to be passed
      as the request body.
    name: Required. The full resource name of the deployment to install.
      Example: `projects/my_project/deployments/my_deployment`.
  """

  googleCloudGsuiteaddonsV1InstallDeploymentRequest = _messages.MessageField('GoogleCloudGsuiteaddonsV1InstallDeploymentRequest', 1)
  name = _messages.StringField(2, required=True)


class GsuiteaddonsProjectsDeploymentsListRequest(_messages.Message):
  r"""A GsuiteaddonsProjectsDeploymentsListRequest object.

  Fields:
    pageSize: The maximum number of deployments to return. The service might
      return fewer than this value. If unspecified, at most 1,000 deployments
      are returned. The maximum possible value is 1,000; values above 1,000
      are changed to 1,000.
    pageToken: A page token, received from a previous `ListDeployments` call.
      Provide this to retrieve the subsequent page. When paginating, all other
      parameters provided to `ListDeployments` must match the call that
      provided the page token.
    parent: Required. Name of the project in which to create the deployment.
      Example: `projects/my_project`.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class GsuiteaddonsProjectsDeploymentsReplaceDeploymentRequest(_messages.Message):
  r"""A GsuiteaddonsProjectsDeploymentsReplaceDeploymentRequest object.

  Fields:
    googleCloudGsuiteaddonsV1Deployment: A GoogleCloudGsuiteaddonsV1Deployment
      resource to be passed as the request body.
    name: The deployment resource name. Example:
      `projects/123/deployments/my_deployment`.
  """

  googleCloudGsuiteaddonsV1Deployment = _messages.MessageField('GoogleCloudGsuiteaddonsV1Deployment', 1)
  name = _messages.StringField(2, required=True)


class GsuiteaddonsProjectsDeploymentsUninstallRequest(_messages.Message):
  r"""A GsuiteaddonsProjectsDeploymentsUninstallRequest object.

  Fields:
    googleCloudGsuiteaddonsV1UninstallDeploymentRequest: A
      GoogleCloudGsuiteaddonsV1UninstallDeploymentRequest resource to be
      passed as the request body.
    name: Required. The full resource name of the deployment to install.
      Example: `projects/my_project/deployments/my_deployment`.
  """

  googleCloudGsuiteaddonsV1UninstallDeploymentRequest = _messages.MessageField('GoogleCloudGsuiteaddonsV1UninstallDeploymentRequest', 1)
  name = _messages.StringField(2, required=True)


class GsuiteaddonsProjectsGetAuthorizationRequest(_messages.Message):
  r"""A GsuiteaddonsProjectsGetAuthorizationRequest object.

  Fields:
    name: Required. Name of the project for which to get the Google Workspace
      Add-on authorization information. Example:
      `projects/my_project/authorization`.
  """

  name = _messages.StringField(1, required=True)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
